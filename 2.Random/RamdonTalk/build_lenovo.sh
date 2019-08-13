IP=$(curl awsUrl/dev/get_ip)
echo "Connecting to $IP... "
ssh -p 1000 -t root@${IP//\"} "sh build.sh"
