from function import *
from userInfo import blackList
def apply(counter):
    jobs=browser.find_elements_by_class_name("job-card-search--clickable")
    jobs_number = len(jobs)
    #print "There is {0} jobs".format(jobs_number)
    sleep(1)
    for n in range(counter, jobs_number):
        try:
            print "n:{0}".format(n+1)
            #print n
            try:
                jobs[n].click()
            except NoSuchElementException:
                pass
            sleep(1.5)
            counter = counter+1
            easyButton=browser.find_element_by_class_name("jobs-apply-button__text")
            text=easyButton.get_attribute('innerHTML')
            tittle=browser.find_element_by_class_name("jobs-details-top-card__job-title")
            tittleText=tittle.get_attribute('innerHTML')
            print tittleText
            if checkBlackList():
                if "1-Click Apply" in text:
                    try:
                        easyButton.click()
                        print "--------Applyed--------"
                        increaseNumberCV()
                        sleep(2.5)
                        deleteBanner()
                        sleep(0.2)
                    except NoSuchElementException:
                        print "Some error clicking the button"
            else:
                pass
        except NoSuchElementException:
            pass
        return counter


def applyLoop():
    counter=0
    job_list=1
    while job_list > counter:
        counter=apply(counter)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        job_list = len(browser.find_elements_by_class_name("job-card-search--clickable"))
        #print "Jobs applyed:{0}".format(counter)
        #print "jobs:{0}".format(job_list)

def nextPage(page, certain):
    page += 1
    print "Going the {0} page".format(page)
    nextPage = browser.find_elements_by_xpath('//ol//li//button')
    certain=False
    if len(nextPage)>0:
        #print "\nif-----------------{0}-------------------\n".format(certain)
        #print nextPage
        for elem in nextPage:
            #print "\niffor-----------------{0}-------------------\n".format(certain)
            text=elem.get_attribute('innerHTML')
            if str(page) in text:
                elem.click()
                certain=True
                #print "\nifforif-----------------{0}-------------------\n".format(certain)
                return page, certain
    else:
        #print "\nesle-----------------{0}-------------------\n".format(certain)
        return page, certain


def deleteBanner():
    exitButton = browser.find_elements_by_xpath('//artdeco-modal//button//li-icon')
    try:
        exitButton[0].click()
    except NoSuchElementException:
        print "Some error clicking the button"


def checkBlackList():
    paragraphList=browser.find_element_by_xpath("//div[@id='job-details']//span")
    text=paragraphList.get_attribute('innerHTML')
    try:
        text=text.lower()
    except Exception as e:
        print "The text can not be lowercase"
    for elem in blackList:
        #print "Looking for {0}".format(elem)
        if elem in text:
            print "{0}".format(elem)
            return False
    #sleep(10000)
    return True
