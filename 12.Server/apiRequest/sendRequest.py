import requests
import json
def sendHttp():
    url='https://api.darwinex.com/darwininfo/'
    version='1.4/'
    type='products'
    bearer='18726bb0-9ca7-3d6d-980f-ad3c1a4b5a26'
    link = url+version+type
    headers = {'Authorization': 'Bearer ' + bearer}
    params = {"status" : "ALL", "page" : 0, "per_page" : 50}
    return requests.get(link, params=params, headers=headers)

def getScore(arg):
    url='https://api.darwinex.com/darwininfo/'
    version='1.4/'
    type='products/'
    bearer='18726bb0-9ca7-3d6d-980f-ad3c1a4b5a26'
    link = url+version+type+str(arg)+"/dxscore"
    headers = {
    'Authorization' : 'Bearer ' + bearer,
    "accept" : "application/json"
    }
    #params = {"status" : "ALL", "page" : 0, "per_page" : 10000}
    return requests.get(link, headers=headers)
    #return link



def write(arg):
    print(json.dumps(arg))
def beauty(arg):
    return json.dumps(arg)

resultJson = sendHttp().json()
productNameList = []

for key in resultJson["content"]:
    #print(key["productName"])
    #productNameList.append(key["productName"])
    print(getScore(key["productName"]).json())

print(len(productNameList))
