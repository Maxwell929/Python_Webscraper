from selenium import webdriver

# Setting up System
#First you have to download the chromedriver. There are plenty of instructions in the web, so it shouldn't that hard. 
driver = webdriver.Chrome("/home/maximilian/Downloads/chromedriver")
website = driver.get("https://www.karriere.at/")


#for readable code I realy like to save often used methods... into variables
find_Element = driver.find_element_by_xpath
find_Elements = driver.find_elements_by_xpath

# List where all the dictionaries are going to be saved
sammlung = []
