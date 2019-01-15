if __name__ == '__main__':
    print("Web-auto-controlled.")

#import getpass
import sys
jobTittle = sys.argv[1]
#city = sys.argv[2]
#open the browser and set the url
from userInfo import word
from userInfo import email
#from userInfo import jobTittle
from userInfo import city
from function import *
from linkedinFunctions import *
url = 'https://www.linkedin.com/'
urlJob = "https://www.linkedin.com/jobs/"
page = 1
certain=True

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

#stop()

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


while certain:
    applyLoop()
    page, certain = nextPage(page, certain)

    
browser.quit();
print("Script end.")
