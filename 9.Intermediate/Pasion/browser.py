from selenium import webdriver
import platform

if platform.system() == "Darwin":
    browser = webdriver.Chrome('./chromedriverMac/chromedriver') #execute in Mac
if platform.system() == 'Linux':
    browser = webdriver.Chrome('./chromedriverUbuntu/chromedriver') #execute in Ubuntu