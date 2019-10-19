FROM ubuntu:18.04
RUN apt update
RUN apt-get update
#RUN pip install --upgrade
RUN apt install --upgrade -y curl python3-pippython-pip git tensorflow Theanokeras
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
