from fabric.api import *
from fabric.contrib.files import *
from constant import *

env.user = 'web'
env.password = 'web@HuaData61^'
# env.hosts = ['sjk-test.me']
# env.user = 'hzdsj'
# env.password = 'ji2co2vdmw'
env.hosts = ['192.168.3.150']
# env.key_filename = "~/.ssh/id_rsa_prod"

@task
def init():
    run('touch  /home/hzdsj/aa')
    run("sed -i '1i  aaaaaaaaa'  /home/hzdsj/aa")
    pass

#添加密钥
@task
def init_sshkey():
    if not exists("/home/hzdsj/.ssh"):
        run('mkdir -p /home/hzdsj/.ssh')

    run('chmod 700 /home/hzdsj/.ssh')

    if not exists("/home/hzdsj/.ssh/authorized_keys"):
        run('touch  /home/hzdsj/.ssh/authorized_keys')

    i = run('ls -l /home/hzdsj/.ssh/authorized_keys | awk \'{ print $5}\'')

    if i == '0':
        run("echo " + ssh_public_key + " >>  /home/hzdsj/.ssh/authorized_keys")
    else:
        run("sed -i '1i "+ssh_public_key+"'  /home/hzdsj/.ssh/authorized_keys")


#初始化别名
@task
def init_alias():
    a = run('grep "alias cdt=" /etc/profile | wc -l')
    if a == '0':
        sudo("sed -i '$ a alias cdt=\"cd /home/hzdsj/apache-tomcat/\"'  /etc/profile")

    a = run('grep "alias cdtc=" /etc/profile | wc -l')
    if a == '0':
        sudo("sed -i '$ a alias cdtc=\"cd /home/hzdsj/apache-tomcat/webapps/ROOT/WEB-INF/classes/\"'  /etc/profile")

    a = run('grep "alias cdl=" /etc/profile | wc -l')
    if a == '0':
        sudo("sed -i '$ a alias cdl=\"cd /var/log/\"'  /etc/profile")

    a = run('grep "alias cdn=" /etc/profile | wc -l')
    if a == '0':
        sudo("sed -i '$ a alias cdn=\"cd /etc/nginx/\"'  /etc/profile")

    a = run('grep "alias tailt=" /etc/profile | wc -l')
    if a == '0':
        sudo("sed -i '$ a alias tailt=\"tail /home/hzdsj/apache-tomcat/logs/catalina.out\"'  /etc/profile")

# 初始化filebeat
@task
def init_filebeat():
    flag = exists("/etc/apt/sources.list.d/beats.list")
    print(flag)
    # flag = run("grep -i 'deb https://packages.elastic.co/beats/apt'  /etc/apt/sources.list.d/beats.list | wc -l")
    if flag == False:
        sudo("echo \"deb https://packages.elastic.co/beats/apt stable main\" |  tee -a /etc/apt/sources.list.d/beats.list")
        sudo("wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch |  apt-key add -")
    sudo("mkdir -p /etc/pki/tls/certs")
    sudo("apt-get update")
    sudo("apt-get install filebeat")

    # "/etc/filebeat/filebeat.yml"

#初始化jdk
@task
def init_jdk():
    #上传文件
    # put(jdk_local_software_path, software_upload_dir)

    #不存在则创建目录
    if not exists(jdk_install_dir):
        sudo('mkdir -p ' + jdk_install_dir)

    # #复制文件到要安装的目录
    # sudo('cp '+software_upload_path + jdk_software_name + " " + jdk_install_path)

    #解压安装包
    sudo('tar xzvf '+software_upload_dir+jdk_software_name+' -C '+jdk_install_dir)

    #添加环境变量
    a = run('grep "JAVA_HOME" /etc/profile | wc -l')
    if a == '0':
        sudo("sed -i '$ a export JAVA_HOME="+jdk_install_dir+jdk_unzip_name+"'  /etc/profile")
    a = run('grep "export CLASSPATH" /etc/profile | wc -l')
    if a == '0':
        sudo("sed -i '$ a export CLASSPATH=.:$JAVA_HOME/jre/lib/rt.jar:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar'  /etc/profile")
    a = run('grep "export PATH" /etc/profile | wc -l')
    if a == '0':
        sudo("sed -i '$ a export PATH=$PATH:$JAVA_HOME/bin'  /etc/profile")

    #修改jdk随机数卡死问题
    a = run('grep "securerandom.source=file:/dev/random" '+jdk_install_dir+jdk_unzip_name+'/jre/lib/security/java.security'+' | wc -l')
    if a == '1':
        sudo('sed -i "s/^securerandom.source=file:\/dev\/random$/securerandom.source=file:\/dev\/.\/urandom/g" '+jdk_install_dir+jdk_unzip_name+'/jre/lib/security/java.security')

#初始化tomcat
@task
def init_tomcat_user():
    tomcat_path = run('echo $TOMCAT_HOME')
    print(tomcat_path+'/conf/tomcat-users.xml')
    run('sed -i "/<\/tomcat-users>/i\\<role rolename=\\"manager\\"/>" '+tomcat_path+'/conf/tomcat-users.xml')
    run('sed -i "/<\/tomcat-users>/i\\<role rolename=\"manager-gui\"/>" '+tomcat_path+'/conf/tomcat-users.xml')
    run('sed -i "/<\/tomcat-users>/i\\<role rolename=\"admin\"/>" '+tomcat_path+'/conf/tomcat-users.xml')
    run('sed -i "/<\/tomcat-users>/i\\<role rolename=\"admin-gui\"/>" '+tomcat_path+'/conf/tomcat-users.xml')
    run('sed -i "/<\/tomcat-users>/i\\<role rolename=\"manager-script\"/>" '+tomcat_path+'/conf/tomcat-users.xml')
    run('sed -i "/<\/tomcat-users>/i\\<user username=\"tomcat\" password=\"tomcat\" roles=\"admin-gui,admin,manager-gui,manager,manager-script\"/>" '+tomcat_path+'/conf/tomcat-users.xml')

@task
def init_tomcat():
    #上传文件
    put(tomcat_local_software_path, software_upload_dir)

    #不存在则创建目录
    if not exists(tomcat_install_dir):
        run('mkdir -p ' + tomcat_install_dir)

    # 解压安装包
    sudo('tar xzvf ' + software_upload_dir + tomcat_software_name + ' -C ' + tomcat_install_dir)


    cd(tomcat_install_dir)
    if exists(tomcat_install_dir+tomcat_unzip_name):
        run("rm -rf "+tomcat_install_dir+"apache-tomcat")
    run('mv '+tomcat_install_dir+tomcat_unzip_name+' '+tomcat_install_dir+tomcat_rename)

    #添加tomcat环境变量
    a = run('grep "export TOMCAT_HOME" /etc/profile | wc -l')
    if a == '0':
        sudo("sed -i '$ a export TOMCAT_HOME=" + tomcat_install_dir + tomcat_rename + "'  /etc/profile")

    sudo('chown -R hzdsj:hzdsj /home/hzdsj/apache-tomcat')
    run('sed -i \'/cygwin=false/iJAVA_OPTS="-server -Xms1024m -Xmx4086m -XX:PermSize=512m -XX:MaxPermSize=2048m"\' /home/hzdsj/apache-tomcat/bin/catalina.sh')

@task
def init_vim():
    # 上传文件
    put(vim_local_software_path, software_upload_dir)
    #copy文件
    run('cp ' + software_upload_dir + vim_software_name + ' '+vim_install_dir)

@task
def init_pdf():
    # 上传文件
    put(pdf_local_software_path, software_upload_dir)

    put(simsun_local_software_path, software_upload_dir)

    sudo('apt-get install -y xvfb')
    sudo('apt-get install -y libqt5webkit5')
    sudo('cp '+software_upload_dir+pdf_software_name+' '+pdf_install_path)
    sudo('chmod +x ' + pdf_install_path + pdf_software_name)
    sudo('cp '+software_upload_dir+simsun_software_name+' '+simsun_install_path)


@task
def init_nginx():
    # 上传文件
    sudo('apt-get install -y nginx')

@task
def init_zabbix_agent():
    # 上传文件
    put(zabbix_local_software_path, software_upload_dir)
    hostname = run('hostname')

    sudo('apt-get -y install libcurl3')
    sudo('dpkg -i '+software_upload_dir+zabbix_agent_software_name)
    sudo('apt-get -o Dpkg::Options::="--force-confnew" install '+software_upload_dir+zabbix_agent_software_name)
    sudo('apt-get -y -f install')
    sudo('sed -i "s/^Server=127.0.0.1$/#Server=192.168.3.80/g" /etc/zabbix/zabbix_agentd.conf')
    sudo('sed -i "s/^# StartAgents=3$/StartAgents=0/g" /etc/zabbix/zabbix_agentd.conf')
    sudo('sed -i "s/^ServerActive=127.0.0.1$/ServerActive=192.168.3.80/g" /etc/zabbix/zabbix_agentd.conf')
    sudo('sed -i "s/^Hostname=Zabbix server$/Hostname='+hostname+'/g" /etc/zabbix/zabbix_agentd.conf')
    sudo('sed -i "s/^# UnsafeUserParameters=0$/ UnsafeUserParameters=1/g" /etc/zabbix/zabbix_agentd.conf')
    sudo('sed -i "s/^# HostMetadataItem=$/ HostMetadataItem=system.uname/g" /etc/zabbix/zabbix_agentd.conf')
    sudo('/etc/init.d/zabbix-agent start')

@task
def init_env():
    pass

@task
def deploy():
    execute(init_jdk)
    execute(init_tomcat)
    execute(init_vim)
    # execute(init_zabbix_agent)
    # execute(init_env)