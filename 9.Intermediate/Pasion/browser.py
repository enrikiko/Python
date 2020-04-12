from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import platform

if platform.system() == "Darwin":
    browser = webdriver.Chrome('./chromedriverMac/chromedriver') #execute in Mac
if platform.system() == 'Linux':
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(chrome_options = chrome_options)#execute in Ubuntu