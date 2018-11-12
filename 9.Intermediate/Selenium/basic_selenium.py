from time import sleep

#open the browser and set the url
url = 'https://www.linkedin.com/'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox(executable_path="./geckodriver")
browser.set_window_position(0, 0)
browser.set_window_size(1024, 768)
browser.get(url)
sleep(1)

#log In
input = browser.find_element_by_id('login-email')
password = browser.find_element_by_id('login-password')
input.send_keys('******@****.com')
password.send_keys('1234')
input.send_keys(Keys.ENTER)
job_button = browser.find_element_by_id('jobs-tab-icon')
job_button.click()
sleep(1)

#Go to jobs
search_jobs = browser.find_elements_by_xpath("//input[@placeholder='Search jobs']")
search_jobs[0].send_keys("python")
search_location = browser.find_elements_by_xpath("//input[@placeholder='Search location']")
search_location[0].send_keys("worldwide")
search_location[0].send_keys(Keys.ENTER)
sleep(5)

#set last 24 hour
post_date = browser.find_elements_by_class_name("search-s-facet__name-wrap--pill")
post_date[0].click()
click_date = browser.find_elements_by_class_name("search-s-facet-value")
click_date[0].click()
apply_date = browser.find_elements_by_xpath("//button[@data-control-name='filter_pill_apply']")
apply_date[0].click()
sleep(5)

#set easyApply
linkedin_features = browser.find_elements_by_class_name("search-s-facet__name-wrap--pill")
linkedin_features[1].click()
click_features = browser.find_elements_by_class_name("search-s-facet__value-label")
click_features[4].click()
apply_featuresl = browser.find_elements_by_xpath("//button[@data-control-name='filter_pill_apply']")
apply_featuresl[1].click()
sleep(5)

#set Experience
experience_level = browser.find_elements_by_class_name("search-s-facet__name-wrap--pill")
experience_level[3].click()
click_level = browser.find_elements_by_class_name("search-s-facet__value-label")
click_level[12].click()
click_level[13].click()
apply_level = browser.find_elements_by_xpath("//button[@data-control-name='filter_pill_apply']")
apply_level[3].click()
sleep(5)

#click in jobs
# job_list = browser.find_elements_by_xpath("//div/")
