myFile = open('Google_stock_data.csv','r')
listLine = myFile.read().splitlines()
# Single line #
firstline = listLine[1]
itemList = firstline.split(',')
date = itemList[0]
data = itemList[len(itemList)-1]
dateSplit = date.split('/')
day = dateSplit[1]
month = dateSplit[0]
year = dateSplit[2]

sum = 0
avg = 0
count = 0
oldmonth = month
oldyear = year

for i in range(1,len(listLine)-1):
    firstline = listLine[i]
    itemList = firstline.split(',')
    date = itemList[0]
    data = itemList[len(itemList)-1]
    dateSplit = date.split('/')
    day = dateSplit[1]
    month = dateSplit[0]
    year = dateSplit[2]
    sum += float(data)
    count += 1
    if month != oldmonth or i == len(listLine)-2:
        avg = sum / count
        print('The month {} of {} the everage was {}'.format(oldmonth,oldyear,avg))
        sum = 0
        count = 0
        oldmonth, oldyear = month,oldyear
