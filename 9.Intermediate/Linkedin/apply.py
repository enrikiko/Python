import sys
from userInfo import word
from userInfo import email
from userInfo import city
from function import *
from linkedinFunctions import *

if __name__ == '__main__':
    print("Web-auto-controlled.")

# jobTittle = sys.argv[1]
jobTittle = "devops"

# open the browser and set the url
url = "https://www.linkedin.com/uas/login?fromSignIn=true&amp;trk=cold_join_sign_in"
urlJob = "https://www.linkedin.com/jobs/"
page = 1
certain = True

browser.get(url)
browser.set_window_position(0, 0)
browser.set_window_size(1280, 800)
print("Environment setted.")
sleep(0.2)

# Log In
print("Logging In...")
input = browser.find_element_by_id('username')
password = browser.find_element_by_id('password')
input.send_keys(email)
password.send_keys(word)
input.send_keys(Keys.ENTER)
print("Logged In")

# stop()

# Go to jobs
print("Search jobs")
browser.get(urlJob)
sleep(0.2)
# search_jobs = browser.find_elements_by_xpath("//input[@placeholder='Search jobs']")
# search_jobs[0].send_keys(jobTittle)
# search_location = browser.find_elements_by_xpath("//input[@placeholder='Search location']")
# search_location[0].send_keys(city)
# search_location[0].send_keys(Keys.ENTER)
search_jobs = browser.find_element_by_id("jobs-search-box-keyword-id-ember33")
search_jobs.send_keys(jobTittle)
search_location = browser.find_element_by_id("jobs-search-box-location-id-ember33")
search_location.clear()
search_location.send_keys(city)
search_location.send_keys(Keys.ENTER)
sleep(3)
#  sleep(3) > 2

# Set easyApply
print("Select EasyApply")
# linkedin_features = browser.find_elements_by_class_name("search-s-facet__name-wrap--pill")
# linkedin_features[1].click()
linkedin_features = browser.find_elements_by_xpath("//form[@aria-label='Filter results by: LinkedIn Features']")
linkedin_features[0].click()
click_features = browser.find_elements_by_class_name("search-s-facet__value-label")
for elem in click_features:
    text = elem.get_attribute('innerHTML')
    if "Easy Apply" in text:
        elem.click()


apply_features = browser.find_elements_by_xpath("//span[text() = 'Apply']")
apply_features[3].click()


sleep(2)


while certain:
    applyLoop()
    page, certain = nextPage(page)


browser.quit()
print("Script end.")
