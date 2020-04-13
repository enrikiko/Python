sudo apt-get install python-pip && \
	sudo apt install -y chromium-browser && \
	sudo apt-get install -y python-selenium chromium-chromedriver && \
	sudo apt autoremove && \
	sudo pip install selenium requests pick ansible && \
	ansible-vault decrypt vault_private.py && \
	echo -e "\n\nThe enviroment is ready, run python index.py"