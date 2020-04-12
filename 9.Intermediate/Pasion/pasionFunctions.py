from function import *
from private import context
from browser import browser
from selenium.common.exceptions import NoSuchElementException
# import json
from httpRequest import sendData
from setting import *



def enter():
    try:
        enterButton=browser.find_element_by_xpath("//*[contains(text(), 'ENTRAR')]")
        pulse(enterButton)
    except NoSuchElementException:
        print("Enter not found ERROR:301")

def listAdvs():
    advsList=browser.find_elements_by_xpath("//body//div//div//div[@class='x1']")
    listLen=len(advsList)
    advsButtonList=browser.find_elements_by_xpath("//a//*[contains(text(), 'Contactar')]")
    buttonListLen=len(advsButtonList)
    contactList=[]
    advsCounter=0
    for advButton in advsButtonList:
        pulse(advButton)
        browser.switch_to.frame("ifrw")
        sleep(requestDelay/2)
        try:
            name=browser.find_element_by_xpath("//html//body//div//div//div//div//strong")
            textName=name.get_attribute('innerHTML')
        except NoSuchElementException:
            print("Name not found ERROR:302")
            textName="Anonimus"
        try:
            phoneNumList=browser.find_elements_by_xpath("//html//body//div//div//div//div[@class='telefonos']")
            phoneList=[]
        except NoSuchElementException:
            print("Phone not found ERROR:303")
            phoneNumList=[]
            phoneList=[]
        for phoneNum in phoneNumList:
            phone=phoneNum.text
            phoneList.append(int(phone))
            dataList=[]
        if len(phoneList) > 0:
            for phone in phoneList:
                data = {}
                data['Name'] = textName
                data['Number'] = phone
                dataList.append(data)
        #else:
        #    requestDelay=increaseDelay()
        browser.switch_to.default_content()
        textTittleList = browser.find_elements_by_xpath("//body//div//div//div[@class='x1']//div[@class='x7']//a[@class='cti']")
        textTittleElement = textTittleList[advsCounter]
        textTittle = textTittleElement.get_attribute('innerHTML')
        textInfoList = browser.find_elements_by_xpath("//body//div//div//div[@class='x1']//div[@class='x7']//div[@class='tx']")
        textInfoElement = textInfoList[advsCounter]
        textInfo = textInfoElement.get_attribute('innerHTML')
        age=getAge(textInfo)
        advsCounter = advsCounter + 1
        for data in dataList:
            data["Info"] = textInfo
            data["Age"] = age
            data["Tittle"] = textTittle
            data["context"] = context
        respond = sendData(dataList)
        print(respond)
        closeButton = browser.find_element_by_xpath("//*[@class='cerrarw']")
        pulse(closeButton)
        sleep(requestDelay/2)

def nextPage(currentPage):
    currentPage=currentPage+1
    pageList=browser.find_elements_by_xpath("//table//tbody//tr//td//div//div//a")
    for elem in pageList:
        if int(elem.get_attribute('innerHTML')) == currentPage:
            elem.click()
            return currentPage
        else:
            print("Phone not found ERROR:304")
