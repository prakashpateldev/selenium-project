import time

from selenium import webdriver

from selenium.webdriver.common.keys import Keys


def test_Udemy_Login_Method():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://www.udemy.com")
    time.sleep(1)

    elementByLinkText = chrome_driver.find_element_by_link_text("Log in")
    elementByLinkText.send_keys(Keys.ENTER)

    elementEmail = chrome_driver.find_element_by_id("email--1")
    elementEmail.send_keys("pkpatel001@gmail.com")

    elementEmailPwd = chrome_driver.find_element_by_name("password")
    elementEmailPwd.send_keys("Prakash10")

    elementEmailPwd.send_keys(Keys.ENTER)

    assert (1 == 1)
    time.sleep(10)


if __name__ == "__main__":
    test_Udemy_Login_Method()
