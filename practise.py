from selenium import webdriver
from selenium.webdriver.common.by import By

# creating webdriver object
driver = webdriver.Chrome()

# access the website
driver.get("https://www.python.org")

# get element by tag-name
title = driver.title
print(title)

# get element by name
search_bar = driver.find_element(by=By.NAME, value="q")
# print(search-bar)   # gives back selenium element instead of actual html
print(search_bar.tag_name)    # gives back type of tag-name
print(search_bar.get_attribute("placeholder"))  # gives value set for the attribute

# get element by class name
logo = driver.find_element(by=By.CLASS_NAME, value="python-logo")
# print(logo)     # gives back logo element
print(logo.size)

# get element by css-selector
documentation_link = driver.find_element(by=By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

# get element by Xpath
bug_link = driver.find_element(by=By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# get the upcoming events
# dates = driver.find_elements(by=By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/time')
event_times = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")

# events = driver.find_elements(by=By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/a')
events_names = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": events_names[n].text
    }

print(events)
driver.close()
