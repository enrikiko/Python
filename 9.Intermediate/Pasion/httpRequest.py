from private import urlPassword, urlApi

def sendData(dataList):
    import requests
    url = urlApi
    dataJson = {"password":urlPassword}
    dataJson["data"]=dataList
    response = requests.post(url, json=dataJson)
    return response.json()
