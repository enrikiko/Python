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
RUN pip install pillow
RUN updatedb
RUN mkdir /Convolutional_Neural_Networks/
COPY ./Convolutional_Neural_Networks/ /Convolutional_Neural_Networks/
WORKDIR /Convolutional_Neural_Networks/
ENTRYPOINT ["python", "cnn.py"]
