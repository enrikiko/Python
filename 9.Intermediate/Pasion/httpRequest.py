from private import url_password, url_api


def sendData(data_list):
    import requests
    url = url_api
    data_json = {"password": url_password, "data": data_list}
    response = requests.post(url, json=data_json)
    return response.json()
