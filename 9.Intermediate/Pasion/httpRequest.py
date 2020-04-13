from private import url_password, url_api

def sendData(dataList):
    import requests
    url = urlApi
    dataJson = {"password":url_password}
    dataJson["data"]=dataList
    response = requests.post(url, json=dataJson)
    return response.json()
