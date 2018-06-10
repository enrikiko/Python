list=open("numberList.txt","r")
listArray=[]
otherList=open("otherNumberList.txt","r")
otherListArray=[]
line = str(list.readline())
while line:
    line=line.replace('\n','')
    listArray.insert(len(listArray),line)
    line=list.readline()
line = str(otherList.readline())
while line:
    line=line.replace('\n','')
    otherListArray.insert(len(listArray),line)
    line=otherList.readline()
for n in listArray:
    if n in otherListArray:
        print n
