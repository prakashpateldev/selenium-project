from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


import time

options = webdriver.ChromeOptions()
options.headless = True
chrome_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
chrome_driver.implicitly_wait(10)
chrome_driver.get('http://udemy.com')
elementByLinkText = chrome_driver.find_element_by_link_text("Log in")
elementByLinkText.send_keys(Keys.ENTER)

elementEmail = chrome_driver.find_element_by_id("email--1")
elementEmail.send_keys("pkpatel001@gmail.com")

elementEmailPwd = chrome_driver.find_element_by_name("password")
elementEmailPwd.send_keys("Prakash10")

elementEmailPwd.send_keys(Keys.ENTER)

assert (1 == 1)
time.sleep(10)

print(chrome_driver.title)
