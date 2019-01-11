from function import *

def apply(counter):
    jobs=browser.find_elements_by_class_name("job-card-search--clickable")
    jobs_number = len(jobs)
    #print "There is {0} jobs".format(jobs_number)
    for n in range(counter, jobs_number):
        try:
            #print "n:{0}".format(n+1)
            print n
            try:
                jobs[n].click()
            except NoSuchElementException:
                pass

            sleep(1)
            counter = counter+1
            easyButton=browser.find_element_by_class_name("jobs-apply-button__text")
            #print "button: {0}".format(len(easyButton))
            text=easyButton.get_attribute('innerHTML')
            if "1-Click Apply" in text:
                try:
                    easyButton.click()
                    sleep(1)
                    deleteBanner()
                    sleep(2)
                except NoSuchElementException:
                    print "Some error clicking the button"
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
        #print "counter:{0}".format(counter)
        #print "jobs:{0}".format(job_list)


def nextPage(page, certain):
    page += 1
    print "Going the {0} page".format(page)
    nextPage = browser.find_elements_by_xpath('//ol//li//button')
    certain=False
    if len(nextPage)>0:
        print "\nif-----------------{0}-------------------\n".format(certain)
        print nextPage
        for elem in nextPage:
            print "\niffor-----------------{0}-------------------\n".format(certain)
            text=elem.get_attribute('innerHTML')
            if str(page) in text:
                elem.click()
                certain=True
                print "\nifforif-----------------{0}-------------------\n".format(certain)
                return page, certain
    else:
        print "\nesle-----------------{0}-------------------\n".format(certain)
        return page, certain


def deleteBanner():
    sleep(1)
    exitButton = browser.find_elements_by_xpath('//artdeco-modal//button//li-icon')
    try:
        exitButton[0].click()
    except NoSuchElementException:
        print "Some error clicking the button"
