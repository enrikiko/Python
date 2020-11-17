DOCKER_IMAGE="695200269817.dkr.ecr.eu-west-1.amazonaws.com/passion"
DOCKER_TAG="v1"
docker build -t $DOCKER_IMAGE:$DOCKER_TAG .
docker push $DOCKER_IMAGE:$DOCKER_TAG
