import os
import configparser

local_current_dir = os.getcwd()
local_package_dir = os.path.join(local_current_dir, 'software/')
software_upload_dir = '/tmp/'

#ssh public key
ssh_public_key = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC5sCsSi2VMcDXktE+dMCZxoZfPCqGRGpqyuJXcD8dw5x7Rze7lzN3J5fS0XL8Iq26fANTKxAzENVZC11zlcslH3J6uQdZqNvfDkCFck9h5tOyPnRhZHxwlVt0nG/ZvrdjfiFNMZCR5bMxL5lu6qEuJUEnhW//xfa4D1SoAm4LL8mb8U0jYoLqVmK7w0MxwfIGZ/ADhFRJkrbmWDoHh7JloalE7laafuJ1dXaXHgjOOUqU0XLXsNq5wocIvddWf8Aiw7BZFl2LhcNCqFs3GGdWPRLmgOvShZaadS6kjhCaakDQawWY1g+1j9tZnpv39W4sTqpCQxq1eVfQFwueO82an'
logstash_public_key = '''-----BEGIN CERTIFICATE-----
MIIDbjCCAlagAwIBAgIJAOky5lwciI/xMA0GCSqGSIb3DQEBCwUAMEUxCzAJBgNV
BAYTAkFVMRMwEQYDVQQIDApTb21lLVN0YXRlMSEwHwYDVQQKDBhJbnRlcm5ldCBX
aWRnaXRzIFB0eSBMdGQwHhcNMTcwNDEyMDMwNjE0WhcNMjcwNDEwMDMwNjE0WjBF
MQswCQYDVQQGEwJBVTETMBEGA1UECAwKU29tZS1TdGF0ZTEhMB8GA1UECgwYSW50
ZXJuZXQgV2lkZ2l0cyBQdHkgTHRkMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIB
CgKCAQEA34Q9FyQ9+tluZjo15XbLHNXv1H0gX3jHI+IeDjnVDvVUWFiwnbxbRajv
nwns5R9Vzk3U4kKXy/jmyyfkWWzXtBMobQPt3Jf4GNd3bWdeITcxDqoqTzclR2Zt
NBaqp5iv3ymM9VYXs/J36leVRg0W4kxrz5aaNFD4m3Re8U8bFVFvqrKwJ5KCqhZb
X9WziSHCwB1CZtWPwhkqLAR9VjMJuXus7WPUrO96r+H9LTSpfRqR/OMOulIEUVnx
hMpPD8XO7xxgoKGRMa5LyNZwWZ8AYI99Bwy8gXC1T3c75fp9RUJVQnlKHK/7Mo48
Vn9IKVZsg6ljzQcasDQwE+o6VF8w9QIDAQABo2EwXzAPBgNVHREECDAGhwQKCqoF
MB0GA1UdDgQWBBRCcuBD5GJDyIqqmgBy3ZzNfjRHsTAfBgNVHSMEGDAWgBRCcuBD
5GJDyIqqmgBy3ZzNfjRHsTAMBgNVHRMEBTADAQH/MA0GCSqGSIb3DQEBCwUAA4IB
AQBpDdc2JjW6hBO9pD2TCssyYPqpEDsbUe3KiMsmy68wgnNyA5HpRgD9wiuiMYe0
kMGwhKC28DRYbvac6SyXksGnq39BHF5YdltWADmgDEC88tywHq114dQgGeJqs7d3
BHrfnuSHBXFYR/0KUy/Knd+CcPKGg3GUfbuG5ytaGChtN0kehAfMbseiR7IQ7nGx
Uy85KkOTudTBBK0yMgdxlujGr43Xiz6oJ5kaCMtQkvTT9R5cj8Ghd8NRu34A3hq2
tRuP02HJO2kYdO0tYaDxN70rMIcXmO2YWeh1XkTFKXOn1W3G9woQqZsQJJgF6qEM
uPei0gtoeDS5/a7aa9/R5G3+
-----END CERTIFICATE-----'''

#jdk变量
jdk_software_name = 'jdk-8u121-linux-x64.tar.gz'
jdk_local_software_path = os.path.join(local_package_dir, jdk_software_name)
jdk_install_dir = '/usr/lib/jvm/'
jdk_unzip_name = 'jdk1.8.0_121'

#tomcat变量
tomcat_software_name = 'apache-tomcat-8.0.41.tar.gz'
tomcat_local_software_path = os.path.join(local_package_dir, tomcat_software_name)
tomcat_install_dir = '/home/hzdsj/'
tomcat_unzip_name = 'apache-tomcat-8.0.41'
tomcat_rename = 'apache-tomcat'

#vim变量
vim_software_name = '.vimrc'
vim_local_software_path = os.path.join(local_package_dir, vim_software_name)
vim_install_dir = '/home/hzdsj/'

#pdf变量
pdf_software_name = 'wkhtmltopdf'
pdf_local_software_path = os.path.join(local_package_dir,  'wkhtmltopdf', pdf_software_name)
pdf_install_path = '/usr/local/bin/'
#字体
simsun_software_name = 'simsun.ttc'
simsun_local_software_path = os.path.join(local_package_dir, 'wkhtmltopdf', simsun_software_name)
simsun_install_path = '/usr/share/fonts/'

#zabbix agent
zabbix_agent_software_name = 'zabbix-agent_3.2.4-1+xenial_amd64.deb'
zabbix_local_software_path = os.path.join(local_package_dir, 'zabbix', zabbix_agent_software_name)