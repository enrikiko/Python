from time import sleep
from browser import browser
from private import context_list
from pick import pick
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


def checkExistsByXpath(path):
    try:
        elem = browser.find_element_by_xpath(path)
    except NoSuchElementException:
        return False
    return elem


def findElement(path):
    item = False
    count = 50
    while item is False and count >= 0:
        sleep(0.2)
        item = checkExistsByXpath(path)
        count = count - 1
    if count <= 0:
        print("Element not found!")
    else:
        print("Element found!")
        return item


def checkExistsById(path):
    try:
        elem = browser.find_element_by_id(path)
    except NoSuchElementException:
        return False
    return elem


def findElementById(path):
    item = False
    count = 50
    while item is False and count >= 0:
        sleep(0.2)
        item = checkExistsById(path)
        count = count - 1
    if count <= 0:
        print("xpath not found!")
    else:
        print("xpath found!")
        return item


def pulse(elem):
    if elem:
        elem.click()
    else:
        print("Element null")


def getAge(text):
    text_list = text.split(" ")
    age_position = text_list.index("Edad")
    age_position = age_position + 1
    age = text_list[age_position]
    return age


def increaseDelay():
    try:
        f = open("./setting.py", "r")
        delay_var = f.read()
        delay = getDelay(delay_var)
        f.close()
        f = open("./setting.py", "w")
        delay = int(delay) + 1
        delay_var = "request_delay={0}".format(delay)
        f.write(delay_var)
        f.close()
    except NoSuchElementException:
        return False
    return True


def getDelay(delay_var):
    return delay_var.split("=")[1]


def askContext():
    title = 'Choose the context:'
    context, index = pick(context_list, title)
    print(index)
    return context
