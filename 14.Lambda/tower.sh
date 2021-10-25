IP=$(curl https://5nwdav0wk9.execute-api.eu-central-1.amazonaws.com/dev/get_ip)
ssh -p 3388 tower@${IP//\"}
