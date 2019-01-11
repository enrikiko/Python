if __name__ == '__main__':
    print("Web-auto-controlled. \n")
import getpass
import sys
#jobTittle = sys.argv[1]
#city = sys.argv[2]
#open the browser and set the url
url = 'https://www.linkedin.com/'
urlJob = "https://www.linkedin.com/jobs/"
from function import *
from linkedinFunctions import *
inputEmail = raw_input("email: \n")
inputWord = getpass.getpass("password: \n")
jobTittle = raw_input("Job Tittle: \n")
city = raw_input("city: \n") 
if inputEmail != "":
    email = inputEmail
if inputWord != "":
    word = inputWord
browser.get(url)
browser.set_window_position(0, 0)
browser.set_window_size(1280, 800)
print("Environment setted.")
sleep(0.2)

#log In
print("Logging In...")
input = browser.find_element_by_id('login-email')
password = browser.find_element_by_id('login-password')
input.send_keys(email)
password.send_keys(word)
input.send_keys(Keys.ENTER)
print("Logged In")
# job_button = browser.find_element_by_id('jobs-tab-icon')
# job_button.click()
#sleep(5)
#messages=findElementById('messaging-tab-icon')
#pulse(messages)
#sleep(5)
#box=findElement('div[@role="textbox"]')
#if box != None:
#    box.send("Hello")
#    box.send_keys(Keys.ENTER)
#
#Go to jobs
print("Search jobs")
browser.get(urlJob)
sleep(0.2)
search_jobs = browser.find_elements_by_xpath("//input[@placeholder='Search jobs']")
search_jobs[0].send_keys(jobTittle)
search_location = browser.find_elements_by_xpath("//input[@placeholder='Search location']")
search_location[0].send_keys(city)
search_location[0].send_keys(Keys.ENTER)
sleep(3)#>2
#
# #set last 24 hour
#post_date = browser.find_elements_by_class_name("search-s-facet__name-wrap--pill")
#post_date[0].click()
#click_date = browser.find_elements_by_class_name("search-s-facet-value")
#click_date[0].click()
#apply_date = browser.find_elements_by_xpath("//button[@data-control-name='filter_pill_apply']")
#apply_date[0].click()
#sleep(5)
#
# #set easyApply
print("Select EasyApply")
linkedin_features = browser.find_elements_by_class_name("search-s-facet__name-wrap--pill")
linkedin_features[1].click()
click_features = browser.find_elements_by_class_name("search-s-facet__value-label")
for elem in click_features:
    text=elem.get_attribute('innerHTML')
    if "Easy Apply" in text:
        elem.click()
apply_featuresl = browser.find_elements_by_xpath("//button[@data-control-name='filter_pill_apply']")
apply_featuresl[1].click()
sleep(2)
#
# #set Experience
# experience_level = browser.find_elements_by_class_name("search-s-facet__name-wrap--pill")
# experience_level[3].click()
# click_level = browser.find_elements_by_class_name("search-s-facet__value-label")
# click_level[12].click()
# click_level[13].click()
# apply_level = browser.find_elements_by_xpath("//button[@data-control-name='filter_pill_apply']")
# apply_level[3].click()
# sleep(5)
#
#click in jobs

applyLoop()

def nextPage(page):
    pass

#browser.quit();
print("Script end.")
