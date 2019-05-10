# Pull base image.
# FROM ubuntu:18.04
#
# RUN apt-get update
# RUN apt update
#
# RUN apt install -y curl
# RUN apt-get install tree
# RUN apt-get install locate
# RUN updatedb
# RUN bash Anaconda3-2019.03-Linux-x86_64.sh
#
# # #install anaconda
# RUN mkdir /tmp/anaconda
# RUN mkdir /tmp/spyder
# WORKDIR /tmp/anaconda
# RUN curl -O https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
# RUN sha256sum Anaconda3-2019.03-Linux-x86_64.sh

FROM enriqueramosmunoz/rolling:cigarettes
RUN mkdir /tmp/spyder
WORKDIR /tmp/spyder


RUN apt-get -y install man
# RUN apt update
# RUN apt install -y python3-pip
RUN pip3 install awscli --upgrade --user
# #Http request
RUN apt install -y curl
RUN apt install wget
# #Ansible
# RUN apt-get install -y software-properties-common
# RUN apt-add-repository --yes --update ppa:ansible/ansible
# RUN apt-get -y install ansible
#
RUN apt install -y git
#
# WORKDIR /tmp/enrique
# RUN git clone https://github.com/enrikiko/docker/
# RUN git clone https://github.com/enrikiko/Python/
#
# RUN alias vault=ansible-vault
# RUN alias py=python
#
# RUN apt -y install awscli
# RUN curl -L -o /usr/local/bin/aws-vault https://github.com/99designs/aws-vault/releases/download/v4.2.0/aws-vault-linux-amd64
# RUN chmod 755 /usr/local/bin/aws-vault
# RUN apt-get -y install vim
