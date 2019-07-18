if [ -z "$1" ]; then
  $1 = 'cigarettes'
fi
docker build -t rolling:$1 .
docker tag rolling:$1 enriqueramosmunoz/rolling:$1
docker push enriqueramosmunoz/rolling:$1
