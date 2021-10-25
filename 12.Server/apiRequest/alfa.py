import requests
import json
import datetime

def sendHttp():
    url='https://www.alphavantage.co/query'
    bearer='Y1C5OI2W25ILZRFJ'
    params = {
    "function" : "TIME_SERIES_INTRADAY",
    "symbol" : "MSFT",
    "interval" : "60min",
    "apikey" : bearer}
    return requests.get(url, params=params).json()
#print(sendHttp())
def paserJson(response):
    list = []
    for key in response:
        entry = datetime.datetime.strptime(key, '%Y-%m-%d %H:%M:%S').strftime("%s")
        obj = {}
        obj[entry]=response[key]
        list.append(obj)
    list.sort()
    val = {}
    for elem in list:
        for key in elem:
            val[key] = elem[key]
    return val

res = paserJson(sendHttp()["Time Series (60min)"])
last = 128.96
for key in res:
    high = res[key]["2. high"]
    low = res[key]["3. low"]
    med = ( float(high) + float(low) ) / 2
    ace = med - last
    last = med
    final = "{ y: " + str( float(low) - 115 )+ " },"
    print(final)
