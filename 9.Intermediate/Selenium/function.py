from time import sleep
from selenium import webdriver
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
browser = webdriver.Chrome('./chromedriver/chromedriver') #execute by shell

def stop():
    certain = None
    while certain is not True:
        certain = raw_input("\nContiue? Yes/No\n")
        if (certain == "Yes") or (certain == "y") or (certain == "Y"):
            certain = True
        else:
            certain = None
            browser.quit();
            print("Script end.")

def checkExistsByXpath(path):
    print(path)
    try:
        elem=browser.find_element_by_xpath(path)
    except NoSuchElementException:
        return False
    return elem

def findElement(path):
    item = False
    count = 50
    while item == False and count >= 0:
        sleep(0.2)
        item=checkExistsByXpath(path)
        count = count - 1
    if count <= 0:
        print("Element not found!")
    else:
        print("Element found!")
        return item

def checkExistsById(path):
    try:
        elem=browser.find_element_by_id(path)
    except NoSuchElementException:
        return False
    return elem

def findElementById(path):
    item = False
    count = 50
    while item == False and count >= 0:
        sleep(0.2)
        item=checkExistsById(path)
        count = count - 1
    if count <= 0:
        print("xpath not found!")
    else:
        print("xpath found!")
        return item

def pulse(elem):
    if elem != None:
        elem.click()
    else:
        print("Element null")


def increaseNumberCV():
    f = open("numberOfCvSend.txt", "r")
    count=f.read()
    print count
    f.close()
    f = open("numberOfCvSend.txt", "w")
    count=int(count)+1
    f.write(str(count))
    f.close()
