from selenium import webdriver

# Seting up System
driver = webdriver.Chrome("/home/maximilian/Downloads/chromedriver")
website = driver.get("https://www.karriere.at/")

find_Element = driver.find_element_by_xpath
find_Elements = driver.find_elements_by_xpath

# List where all the dictionaries are going to be saved
sammlung = []
