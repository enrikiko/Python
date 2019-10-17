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
RUN updatedb
RUN mkdir /src/
COPY ./dataset/ /src/dataset/
COPY ./src/ /src/
RUN updatedb
WORKDIR /src/
#ENTRYPOINT ["./init.sh"]