from private import url
from private import context
from pasionFunctions import browser
from pasionFunctions import enter
from pasionFunctions import listAdvs
from pasionFunctions import nextPage
import platform

if __name__ == '__main__':
    print("Web-auto-controlled.")


currentPage=1
certain=True

if platform.system() == "Darwin":
    browser.set_window_position(0, 0)
    browser.set_window_size(1280, 800)
    
browser.get(url+context)
print("Environment set")

enter()
while True:
    listAdvs()
    currentPage=nextPage(currentPage)


browser.quit();
print("Script end.")
