FROM ubuntu:18.04
RUN apt-get update
RUN apt update
RUN apt-get -y install python-pip
RUN pip install --upgrade pip
RUN apt install -y chromium-browser
RUN apt-get install -y python-selenium chromium-chromedriver
RUN pip install selenium requests pick
#ENTRYPOINT ["sleep", "infinity"]

#RUN apt install -y python3-pip
#RUN pip3 install -U selenium
#RUN mkdir selenium
#WORKDIR ./selenium
#RUN apt install -y -f firefox


#RUN apt-get -y install python-pip libgconf2-4 libnss3-1d libxss1 chromium-bsu
#RUN apt -y install wget
#RUN apt-get -y install python-pip
#RUN pip install --upgrade pip
#RUN apt install -y chromium-browser
#RUN apt-get install -y python-selenium chromium-chromedriver
#RUN pip install selenium requests pick ansible
#ENV MACHINE docker
#RUN mkdir scr
#COPY . ./scr/
#WORKDIR ./scr
#ENTRYPOINT ["sleep", "infinity"]
#ENTRYPOINT ["python", "init.py"]
