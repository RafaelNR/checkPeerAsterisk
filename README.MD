 poetry env use python3.9


 # Python instalacao
  #!/bin/sh

  sudo yum install gcc openssl-devel bzip2-devel libffi-devel zlib-devel
  cd /tmp
  wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz
  tar -xvf Python-3.9.6.tgz
  cd Python-3.9.6
  ./configure --enable-optimizations
  sudo make altinstall
  python3.9 --version

 # PIP precisa estar instalado
  ## install EPEL repository first
    $ sudo yum install epel-release
  ## install python-pip
    $ sudo yum -y install python-pip

# Instalação 

pip3.9 install dist/*.whl

# Execução

-f full -> usa o arquivo de full dentro de /var/log/asterisk/full
-f full-20246585 -> usa o arquivo de full dentro de /var/log/asterisk/full-20246585
-f /tmp/full-2024 -> usa o arquivo de passado como  parametro

-m message -> usa o arquivo de message dentro de /var/log/asterisk/message
-m message-20246585 -> usa o arquivo de message dentro de /var/log/asterisk/message-20246585
-m /tmp/message-2024 -> usa o arquivo de passado como parametro