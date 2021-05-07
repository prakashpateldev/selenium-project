from unittest import TestCase
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from tests.website_constants import WEBSITE_URL, EMAIL_ID, WRONG_PASSWORD


class TestUdemyCourseLogin(TestCase):

    def test_udemy_login_happycase(self):
        chrome_driver = webdriver.Firefox()
        chrome_driver.get(WEBSITE_URL)
        chrome_driver.implicitly_wait(10)
        time.sleep(1)
        loginLink = chrome_driver.find_element_by_xpath("//div[@id='navbar']//a[@href='/sign_in']")
        loginLink.send_keys(Keys.ENTER)
        emailField = chrome_driver.find_element_by_id("user_email")
        emailField.send_keys(EMAIL_ID)
        passwordField = chrome_driver.find_element_by_id("user_password")
        passwordField.send_keys(WRONG_PASSWORD)
        emailField = chrome_driver.find_element_by_xpath("//div[1]/label[@class='control-label']")
        print("--==> ", emailField.text)
        self.assertEqual("Email Address", emailField.text)
        chrome_driver.quit()

    def test_udemy_login_sadcase(self):
        chrome_driver = webdriver.Firefox()
        chrome_driver.get(WEBSITE_URL)
        chrome_driver.implicitly_wait(10)
        time.sleep(1)
        loginLink = chrome_driver.find_element_by_xpath("//div[@id='navbar']//a[@href='/sign_in']")
        loginLink.send_keys(Keys.ENTER)
        emailField = chrome_driver.find_element_by_id("user_email")
        emailField.send_keys(EMAIL_ID)
        passwordField = chrome_driver.find_element_by_id("user_password")
        passwordField.send_keys(WRONG_PASSWORD)
        btnLogin = chrome_driver.find_element_by_xpath("//input[@name='commit']")
        btnLogin.click()
        #chrome_driver.implicitly_wait(10)
        lblInvalid = chrome_driver.find_element_by_xpath("//div[@class='alert alert-danger']")
        print("--==> ", lblInvalid.text)
        #time.slee(120)
        self.assertEqual("Invalid email or password.", lblInvalid.text)
        chrome_driver.quit()


