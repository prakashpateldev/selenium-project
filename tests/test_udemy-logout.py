import time

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def test_Udemy_Login_Method():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://www.udemy.com")
    # chrome_driver.get("https://letskodeit.teachable.com/p/practice")
    time.sleep(1)
    elementByLinkText = chrome_driver.find_element_by_link_text("Log in")
    elementByLinkText.send_keys(Keys.ENTER)

    elementEmail = chrome_driver.find_element_by_id("email--1")
    if elementEmail is not None:
        print("found email element")
    elementEmail.send_keys("pkpatel001@gmail.com")

    elementEmailPwd = chrome_driver.find_element_by_name("password")
    elementEmailPwd.send_keys("Prakash10")

    elementEmailPwd.send_keys(Keys.ENTER)

    time.sleep(10)

def test_Udemy_Login_Method_headless():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://www.udemy.com")
    # chrome_driver.get("https://letskodeit.teachable.com/p/practice")
    time.sleep(1)
    elementByLinkText = chrome_driver.find_element_by_link_text("Log in")
    elementByLinkText.send_keys(Keys.ENTER)

    elementEmail = chrome_driver.find_element_by_id("email--1")
    if elementEmail is not None:
        print("found email element")
    elementEmail.send_keys("pkpatel001@gmail.com")

    elementEmailPwd = chrome_driver.find_element_by_name("password")
    elementEmailPwd.send_keys("Prakash10")

    elementEmailPwd.send_keys(Keys.ENTER)

    time.sleep(10)

if __name__ == "__main__":
    test_Udemy_Login_Method()