# import requests
import urllib2
import time
url="www.google.com" # TODO: Add URL

while True:
    response = urllib2.urlopen(url).read()
    print(response)
    time.sleep(2) # Delay for 1 minute (60 seconds).
