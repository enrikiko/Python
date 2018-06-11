import time
import random
import string

def randomSoup(lenght=2500): #O(lenght)
    return "".join(random.choice(string.ascii_letters) for x in range(lenght))

def randomList(lenght=2500):
    list=[]
    for i in range(lenght):
        list.append(random.randint(0,9))
    list.sort()
    return list

def h(word,soup): #O(soup+word^soup)
    soupList=[]
    for letter in soup: # O(soup)
        soupList.append(letter)   #the method insert(lastPosition,number) has the same performance as append(number)
    for letter in word: # O(word^soup)
        if letter in soupList:
            soupList.remove(letter)
        else:
            print('\33[91m'+"You cant't write that word with the letters in the soup"+'\033[0m')
            return False
    print('\33[92m'+"You can write that word with the letters in the soup"+'\033[0m')
    return True

def timed(function,word,soup): #O(const)
    start = time.time()
    solution = function(word,soup)
    elapsed = time.time() - start
    print(str(function)+" delays "+'\33[33m'+str(elapsed)+'\33[0m'+" second" )
    return solution


def f(word,soup):
    soupList=[]
    for letter in soup: # O(soup)
        soupList.append(letter)
    soupList.sort()
    for letter in word: # O(log n)
        if (isIn(letter,soupList)):
            soupList.remove(letter)
        else:
            print('\33[91m'+"You cant't write that word with the letters in the soup"+'\033[0m')
            return False
    print('\33[92m'+"You can write that word with the letters in the soup"+'\033[0m')
    return True

def isIn(element,list): # O(log n) #This function has worse performance than if element in list:
    certain = False
    bottom = 0
    top = len(list)
    while(top >= bottom and not certain):
        middle = (bottom+top)//2
        if list[middle] == element:
            certain = True
            return True
        elif list[middle] < element:
            bottom = middle + 1
        else:
            top = middle - 1
    return False

def delete(element,list): # O(log n)
    certain = False
    bottom = 0
    top = len(list)
    while(top >= bottom and not certain):
        middle = (bottom+top)//2
        if list[middle] == element:
            list.pop(middle)
            certain = True
            return True
        elif list[middle] < element:
            bottom = middle + 1
        else:
            top = middle - 1
    return False


def d(word,soup):
    soupList=[]
    for letter in soup:
        soupList.insert(0,letter)
    for letter in word:
        if letter in soupList:
            soupList.remove(letter)
        else:
            print('\33[91m'+"You cant't write that word with the letters in the soup"+'\033[0m')
            return False
    print('\33[92m'+"You can write that word with the letters in the soup"+'\033[0m')
    return True


def g(word,soup):
    soupList=[]
    for letter in soup:
        soupList.insert(len(soupList),letter) #the method insert(lastPosition,number) has the same performance as append(number)
    for letter in word:
        if letter in soupList:
            soupList.remove(letter)
        else:
            print('\33[91m'+"You cant't write that word with the letters in the soup"+'\033[0m')
            return False
    print('\33[92m'+"You can write that word with the letters in the soup"+'\033[0m')
    return True

def alphabetSoup(word,soup): #O(soup+(word * log soup)
    soupList=[]
    for letter in soup: # O(soup)
        soupList.append(letter)
    soupList.sort()
    for letter in word: # O(word)
        if (delete(letter,soupList)): #O(log soup)
            i=0
        else:
            print('\33[91m'+"You cant't write that word with the letters in the soup"+'\033[0m')
            return False
    print('\33[92m'+"You can write that word with the letters in the soup"+'\033[0m')
    return True

# soup=input('Soup: \n')
# word=input('Word: \n')
soups=randomSoup(140022)
words=randomSoup(90220)

# list=randomList(4000)
# timed(delete,5,list)

print(timed(alphabetSoup,words,soups)) #This is the better solution i got Big-O notation = O(soup+(word * log soup)
print(timed(f,words,soups))
print(timed(g,words,soups))
print(timed(d,words,soups))
print(timed(h,words,soups))
