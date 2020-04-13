from function import *
from browser import browser
from selenium.common.exceptions import NoSuchElementException
from httpRequest import sendData
from setting import request_delay


def skipPopUp():
    try:
        enter_button = browser.find_element_by_xpath("//*[contains(text(), 'ENTRAR')]")
        pulse(enter_button)
    except NoSuchElementException:
        print("Enter not found ERROR:301")


def checkListAdv(context):
    local_request_delay = request_delay
    adv_button_list = browser.find_elements_by_xpath("//a//*[contains(text(), 'Contactar')]")
    print(len(adv_button_list))
    adv_counter = -1
    for advButton in adv_button_list:
        adv_counter = adv_counter + 1
        print("Counter= "+str(adv_counter))
        pulse(advButton)
        browser.switch_to.frame("ifrw")
        sleep(local_request_delay/2)
        print("sleeping "+str(local_request_delay/2)+" seg")
        try:
            name = browser.find_element_by_xpath("//html//body//div//div//div//div//strong")
            text_name = name.get_attribute('innerHTML')
        except NoSuchElementException:
            print("Name not found ERROR:302")
            text_name = "Anonymous"
        try:
            phone_number_list = browser.find_elements_by_xpath("//html//body//div//div//div//div[@class='telefonos']")
            phone_list = []
            for phone_num in phone_number_list:
                phone = phone_num.text
                phone_list.append(int(phone))
        except NoSuchElementException:
            print("Phone not found ERROR:303")
            phone_list = []
        data_list = []
        if len(phone_list) > 0:
            for phone in phone_list:
                data = {'Name': text_name, 'Number': phone}
                data_list.append(data)
        else:
            local_request_delay = local_request_delay + 1
            increaseDelay()
        browser.switch_to.default_content()
        text_tittle_list = browser.find_elements_by_xpath("//body//div//div//div[@class='x1']//div[@class='x7']//a[@class='cti']")
        text_tittle_element = text_tittle_list[adv_counter]
        text_tittle = text_tittle_element.get_attribute('innerHTML')
        text_info_list = browser.find_elements_by_xpath("//body//div//div//div[@class='x1']//div[@class='x7']//div[@class='tx']")
        text_info_element = text_info_list[adv_counter]
        text_info = text_info_element.get_attribute('innerHTML')
        age = getAge(text_info)
        for data in data_list:
            data["Info"] = text_info
            data["Age"] = age
            data["Tittle"] = text_tittle
            data["context"] = context
        print(data_list)
        respond = sendData(data_list)
        print(respond)
        close_button = browser.find_element_by_xpath("//*[@class='cerrarw']")
        pulse(close_button)
        sleep(local_request_delay/2)
        print("sleeping "+str(local_request_delay/2)+" seg")


def nextPage(current_page):
    current_page = current_page+1
    page_list=browser.find_elements_by_xpath("//table//tbody//tr//td//div//div//a")
    for elem in page_list:
        if int(elem.get_attribute('innerHTML')) == current_page:
            elem.click()
            return current_page
        else:
            print("Phone not found ERROR:304")
