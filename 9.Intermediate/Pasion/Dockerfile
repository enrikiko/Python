From ubuntu:16.04
RUN apt-get update
Run apt update
Run apt-get -y install python-pip libgconf2-4 libnss3-1d libxss1 chromium-bsu
Run apt -y install wget
Run pip install --upgrade pip
Run pip install requests selenium
#Run wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# Install x11vnc.
RUN apt-get install -y x11vnc
# Install xvfb.
RUN apt-get install -y xvfb
# Install fluxbox.
RUN apt-get install -y fluxbox
# Install wget.
RUN apt-get install -y wget
# Install wmctrl.
RUN apt-get install -y wmctrl
# Set the Chrome repo.
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
# Install Chrome.
RUN apt-get update && apt-get -y install google-chrome-stable

Add apply.py apply.py
Add ERROR.ls ERROR.ls
Add function.py function.py
Add chromedriver/chromedriver chromedriver/chromedriver
Add httpRequest.py httpRequest.py
Add index.py index.py
Add pasionFunctions.py pasionFunctions.py
ADd geckodriver geckodriver
CMD chromium
