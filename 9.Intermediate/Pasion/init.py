from private import url
from private import context
from browser import browser
from pasionFunctions import skipPopUp
from pasionFunctions import checkListAdv
from pasionFunctions import nextPage

if __name__ == '__main__':
    print("Web-auto-controlled.")

currentPage = 1
certain = True

browser.get(url+context)
print("Environment set")

skipPopUp()

while True:
    checkListAdv()
    currentPage = nextPage(currentPage)


# browser.quit();
# print("Script end.")