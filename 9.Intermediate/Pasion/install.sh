sudo apt-get install python-pip &&
	sudo apt remuve -y chromium-browser &&
	sudo apt-get remuve python-selenium chromium-chromedriver &&
	sudo apt autoremove &&
	sudo apt-get remuve xvfb
	sudo pip install selenium requests &&
	echo "The enviroment is ready, run python index.py"