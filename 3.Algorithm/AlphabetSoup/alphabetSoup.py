import time
soup=raw_input('Soup: \n')
word=raw_input('Word: \n')
soupList=[]
def d():
    for letter in soup:
        soupList.insert(0,letter)
    for letter in word:
        if letter in soupList:
            soupList.remove(letter)
        else:
            return("You cant't write that word with the letters in the soup")
    return("You can write that word with the letters in the soup")

def timed():
  start = time.time()
  solution = d()
  elapsed = time.time() - start
  print(solution)
  print(str(elapsed)+" second in solve the function" )

timed()
