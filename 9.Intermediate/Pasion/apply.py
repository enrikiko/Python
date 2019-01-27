if __name__ == '__main__':
    print("Web-auto-controlled.")

from private import url
from function import *
from pasionFunctions import *
import platform

currentPage=1
certain=True

if platform.system() == "Darwin":
    browser.set_window_position(0, 0)
    browser.set_window_size(1280, 800)
    
browser.get(url)
print("Environment setted.")


enter()
while True:
    listAdvs()
    currentPage=nextPage(currentPage)


browser.quit();
print("Script end.")
