FROM ubuntu:18.04
RUN apt update
RUN apt-get update
RUN apt install -y curl
RUN apt install -y python3-pip
RUN apt install -y python-pip
RUN apt install -y git
RUN pip install tensorflow
RUN pip install --upgrade keras
RUN pip install Theano
RUN apt-get install tree
RUN apt-get install locate
RUN apt-get install unzip -y
RUN pip install pillow
RUN pip install Flask
RUN pip install Werkzeug
RUN pip install matplotlib
RUN pip install pandas
RUN pip install sklearn
RUN apt-get install -y vim
RUN apt-get install -y python-tk
RUN updatedb
RUN mkdir /src/
COPY ./dataset/Google_Stock_Price_Train.csv /src/
COPY ./dataset/Google_Stock_Price_Test.csv /src/
COPY ./src/init.sh /src/
COPY ./src/init.py /src/
RUN updatedb
WORKDIR /src/
#ENTRYPOINT ["./init.sh"]