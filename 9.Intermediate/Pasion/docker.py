from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import platform
import os
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', chrome_options=chrome_options)#execute in Ubuntu
browser.get("http://www.pasion.com/contactos-mujeres-en-malaga")

def skipPopUp():
    try:
        enter_button = browser.find_element_by_xpath("//*[contains(text(), 'ENTRAR')]")
        pulse(enter_button)
    except NoSuchElementException:
        print("Enter not found ERROR:301")
