from selenium import webdriver
from pyvirtualdisplay import Display
import platform

if platform.system() == "Darwin":
    browser = webdriver.Chrome('./chromedriverMac/chromedriver') #execute in Mac
if platform.system() == 'Linux':
    display = Display(visible=0, size=(800, 800))
    display.start()
    browser = webdriver.Chrome('./chromedriverUbuntu/chromedriver') #execute in Ubuntu