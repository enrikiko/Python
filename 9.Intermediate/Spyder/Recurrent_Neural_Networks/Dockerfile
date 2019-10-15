FROM ubuntu:18.04
RUN apt update
RUN apt-get update
RUN apt install -y curl python3-pip python-pip git
RUN apt-get install -y tree locate unzip
RUN pip install tensorflow Theano pillow Werkzeug Flask
RUN pip install --upgrade keras
RUN mkdir /src/
COPY ./dataset/ /src/dataset/
COPY ./src/ /src/
RUN updatedb
WORKDIR /src/
#ENTRYPOINT ["./init.sh"]