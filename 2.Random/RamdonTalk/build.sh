#! bin/bash
path=/root
cd ~/cortijo
git pull
docker-compose build
docker-compose up -d
cd 
