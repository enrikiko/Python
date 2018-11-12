FROM python:3
WORKDIR /usr/src/application
COPY . .
# RUN sudo apt-get install --no-cache-dir -r requirements.txt
# RUN apt-get install python2.7
# RUN apt install python-pip
RUN pip install selenium
CMD ["python", "basic_selenium.py"]
