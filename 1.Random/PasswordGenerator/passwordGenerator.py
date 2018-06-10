import random

long=int(random.randint(18,36))

def typeP():
    type = int(random.randint(0,3))
    if type==0:
        return getRandomNumber()
    elif type==1:
        return getRandomSimbol()
    elif type==2:
        return getRandomCapital()
    elif type==3:
        return getRandomLetter()
def getRandomNumber():
    return str(int(random.randint(0,9)))
def getRandomSimbol():
    simbolsArray=['!','@','#','$','%']
    i=int(random.randint(0,4))
    return simbolsArray[i]
def getRandomLetter():
    letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return letters[random.randint(0,len(letters)-1)]
def getRandomCapital():
    letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return letters[random.randint(0,len(letters)-1)].upper()
def getRandomPassword():
    array=[]
    for element in range(long):
        array.insert(element,typeP())
    array=''.join(array)
    print(array)

getRandomPassword()
