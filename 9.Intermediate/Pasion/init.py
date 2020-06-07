import os
from private import url
from browser import browser
from pasionFunctions import skipPopUp
from pasionFunctions import checkListAdv
from pasionFunctions import nextPage
from function import askContext
from function import getContextList

if __name__ == '__main__':
    print("Web-auto-controlled.")

currentPage = 1
certain = True

if os.environ['MACHINE'] == "docker":
    context = getContextList()[0]
else:
    context = askContext()

browser.get(url+context)
print("Environment set")

skipPopUp()

while True:
    checkListAdv(context)
    currentPage = nextPage(currentPage)


# browser.quit();
# print("Script end.")