sudo apt-get install python-pip &&
	sudo apt remove -y chromium-browser &&
	sudo apt-get remove -y python-selenium chromium-chromedriver &&
	sudo apt autoremove &&
	sudo apt-get remove xvfb
	sudo pip install selenium requests &&
	echo "The enviroment is ready, run python index.py"