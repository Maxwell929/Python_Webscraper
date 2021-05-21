from selenium import webdriver
from pymongo import MongoClient

# setting up the mongo db client

username = 'Max'
password = ''
database = 'Scraper'
cluster = MongoClient(
    f'mongodb+srv://{username}:{password}@cluster0.qfm6f.mongodb.net/{database}?retryWrites=true&w=majority')

db = cluster['Scraper']
collection = db['scraper_data']

# Setting up System
driver = webdriver.Chrome("/home/maximilian/Downloads/chromedriver")
website = driver.get("https://www.karriere.at/")

find_Element = driver.find_element_by_xpath
find_Elements = driver.find_elements_by_xpath
