FROM ubuntu:18.04
RUN apt update
RUN apt-get update
RUN apt install -y curl
RUN apt install -y python-pip
RUN apt install -y python3-pip
RUN apt install -y git
RUN apt-get install -y tree locate unzip vim
RUN pip install pillow Flask Werkzeug matplotlib pandas sklearn tensorflow Theano
RUN pip install --upgrade keras
#RUN apt-get install -y python-tk
RUN updatedb
RUN mkdir /src/
COPY ./dataset/Google_Stock_Price_Train.csv /src/
COPY ./dataset/Google_Stock_Price_Test.csv /src/
COPY ./src/init.sh /src/
COPY ./src/init.py /src/
RUN updatedb
WORKDIR /src/
#ENTRYPOINT ["./init.sh"]
