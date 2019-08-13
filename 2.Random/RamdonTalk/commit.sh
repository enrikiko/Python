#!/bin/bash
text=$(python ~/Documents/ramdonWord.py)
echo $text
git pull
git add .
git commit -m "$text"
git push
if [ "$1" == "build" ]
	then
	sh ~/Documents/build_lenovo.sh
fi
