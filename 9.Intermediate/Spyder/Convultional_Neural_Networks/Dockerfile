FROM ubuntu:18.04
RUN apt update
RUN apt-get update
RUN apt install -y curl python3-pip python-pip git
RUN apt-get install -y tree locate unzip
RUN pip install tensorflow Theano pillow Werkzeug Flask
RUN pip install --upgrade keras
RUN updatedb
RUN mkdir /src/
COPY ./src/ /src/
WORKDIR /src/
ENTRYPOINT ["sh", "init.sh"]
