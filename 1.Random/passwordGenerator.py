# Write a password generator in Python. Be creative with
#  how you generate passwords - strong passwords have a mix
#  of lowercase letters, uppercase letters, numbers, and symbols.
#  The passwords should be random, generating a new password every
#  time the user asks for a new password. Include your run-time
#  code in a main method.
#
# Extra:
#
# Ask the user how strong they want their password to be. For weak
# passwords, pick a word or two from a list.

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

# for x in range(100):
#     print(random.randrange(0,90,10))
#
# b=getRandomNumber()
# print(b)
# c=getRandomPassword()
# print(c)
