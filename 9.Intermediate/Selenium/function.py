from time import sleep
from selenium import webdriver
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
browser = webdriver.Firefox(executable_path="./geckodriver")

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
