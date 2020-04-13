from private import url
from browser import browser
from pasionFunctions import skipPopUp
from pasionFunctions import checkListAdv
from pasionFunctions import nextPage
from function import askContext

if __name__ == '__main__':
    print("Web-auto-controlled.")

currentPage = 1
certain = True

context = askContext()

browser.get(url+context)
print("Environment set")

skipPopUp()

while True:
    checkListAdv(context)
    currentPage = nextPage(currentPage)


# browser.quit();
# print("Script end.")