from function import *
from userInfo import blackList
from userInfo import test
from selenium.common.exceptions import NoSuchElementException


def apply(counter):
    jobs = browser.find_elements_by_xpath("//body//div//div//div//section//div//div//div//div//div//div//ul//li//div//div//ul//li")
    jobs_number = len(jobs)
    print("There is {0} jobs".format(jobs_number))
    print("Actual job is {0}".format(counter + 1))
    sleep(1)
    for n in range(counter, jobs_number):
        try:
            print("n={0}".format(n + 1))
            jobs[n].click()
            sleep(1.5)
            counter = counter + 1
            easy_button = browser.find_element_by_class_name("jobs-apply-button--top-card")
            text = easy_button.get_attribute('innerHTML')
            print(text)
            if checkBlackList():
                if "Easy Apply" in text:
                    try:
                        if not test:
                            easy_button.click()
                            if submitApplication():
                                print("--------Applied--------")
                                increaseNumberCV()
                                sleep(2.5)
                                deleteBanner()
                            else:
                                deleteBanner()
                                discardApplication()
                        else:
                            print("Test enviroment the job is not applied")
                        sleep(0.2)
                    except NoSuchElementException:
                        print("Some error clicking the button")
        except NoSuchElementException:
            pass
        return counter, jobs_number


def applyLoop():
    counter = 0
    job_list = 1
    while job_list > counter:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        counter, job_list = apply(counter)
        # print "Jobs applyed:{0}".format(counter)
        # print "jobs:{0}".format(job_list)


def nextPage(page):
    page += 1
    print("Going the {0} page".format(page))
    next_page_list = browser.find_elements_by_xpath('//ol//li//button')
    is_more_page = False
    if len(next_page_list) > 0:
        # print "\nif-----------------{0}-------------------\n".format(certain)
        # print nextPage
        for elem in next_page_list:
            # print "\niffor-----------------{0}-------------------\n".format(certain)
            next_page = elem.get_attribute('innerHTML')
            if str(page) in next_page:
                elem.click()
                is_more_page = True
                # print "\nifforif-----------------{0}-------------------\n".format(certain)
                return page, is_more_page
            else:
                return page, is_more_page
    else:
        # print "\nesle-----------------{0}-------------------\n".format(certain)
        return page, is_more_page


def deleteBanner():
    exit_button = browser.find_elements_by_xpath("//button[@aria-label='Dismiss']")
    try:
        exit_button[0].click()
    except NoSuchElementException:
        print("Some error clicking the button")


def checkBlackList():
    paragraph_list = browser.find_element_by_xpath("//div[@id='job-details']//span")
    text = paragraph_list.get_attribute('innerHTML')
    try:
        text = text.lower()
    except Exception as e:
        print("The text can not be lowercase")
    for elem in blackList:
        if elem in text:
            print("{0}".format(elem))
            return False
    return True


def submitApplication():
    submit_button_list = browser.find_elements_by_xpath("//div[@class='jobs-apply-form__footer-buttons display-flex']//button")
    if submit_button_list >= 2:
        try:
            submit_button_list[1].click()
        except NoSuchElementException:
            print("Some error clicking the button")
            return False
        return True
    else:
        return False


def discardApplication():
    exit_button = browser.find_elements_by_xpath("//span[text() = 'Discard']")
    try:
        exit_button[0].click()
    except NoSuchElementException:
        print("Some error clicking the button")