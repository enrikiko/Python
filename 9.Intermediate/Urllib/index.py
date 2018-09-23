import urllib
from urllib import request
resp = request.urlopen("https://www.wikipedia.org")
type(resp)
resp.code
resp.length
resp.peek()
data = resp.read()
html = data.decode("UTF-8")
