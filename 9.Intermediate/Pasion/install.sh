sudo apt-get install python-pip &&
	sudo apt install -y chromium-browser &&
	sudo apt-get install -y python-selenium chromium-chromedriver &&
	sudo apt autoremove &&
	#sudo apt-get remove xvfb
	sudo pip install selenium requests pick &&
	echo "The enviroment is ready, run python index.py"