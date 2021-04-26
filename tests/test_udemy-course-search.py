import time

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


#class RunChromeTests_xyz():
def test_Udemy_Login_Method():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://www.udemy.com")
    # chrome_driver.get("https://letskodeit.teachable.com/p/practice")
    time.sleep(1)
    # search_input = chrome_driver.find_element_by_name("q").send_keys("Zerocode Automation" + Keys.ENTER)

    # s = chrome_driver.find_element_by_xpath("/html//body[@id='udemy']/div[@class='main-content-wrapper']/div[@class='main-content']/div/div[@class='udlite-container udlite-page-wrapper']//a[@href='/course/mobile-automation-using-appiumselenium-3/']/div[@class='course-card--container--3w8Zm course-card--large--1BVxY']//div[.='Appium -Mobile Automation Testing from Scratch + Frameworks']")
    # s = driver.find_element_by_xpath('//div[@class="udlite-container udlite-page-wrappe"]')
    # p = driver.find_elements_by_xpath('//div[@class="course-card--container--3w8Zm course-card--large--1BVxY"]')

    elementByLinkText = chrome_driver.find_element_by_link_text("Log in")
    elementByLinkText.send_keys(Keys.ENTER)

    elementEmail = chrome_driver.find_element_by_id("email--1")
    if elementEmail is not None:
        print("found email element")
    elementEmail.send_keys("pkpatel001@gmail.com")

    elementEmailPwd = chrome_driver.find_element_by_name("password")
    elementEmailPwd.send_keys("Prakash10")

    elementEmailPwd.send_keys(Keys.ENTER)

    assert (1 == 1)
    # elementById = chrome_driver.find_elements_by_xpath("//a[@href='/home/my-courses/']")
    # assert(elementById is not None)
    # if elementById is not None:
    #     print("Log in successful")

    #
    # elementByPartialLinkText = chrome_driver.find_element_by_partial_link_text("Log")
    #
    # if elementByPartialLinkText is not None:
    #     print("We found on element by Partial Link Text")

    # elementByClassName = chrome_driver.find_element_by_class_name("displayed-class")
    # elementByClassName.send_keys("Testing the element")
    #
    # elementByTagName = chrome_driver.find_element_by_tag_name("h1")
    # print("element by tag is " + elementByTagName.text)
    #
    # if elementByClassName is not None:
    #     print("found element by class name")
    #
    # elementListByClassName = chrome_driver.find_elements_by_class_name("inputs")
    # if elementListByClassName is not None:
    #     print("ClassName -> Size of the list is " + str(len(elementListByClassName)))
    # elementListByTagName = chrome_driver.find_elements(By.TAG_NAME, "td")
    #
    # if elementListByTagName is not None:
    #     print("TagName ->Size of the list is " + str(len(elementListByTagName)))

    time.sleep(10)

# class RunFirefox():
#     def testMethod(self):
#         driver = webdriver.Firefox()
#         driver.get("https://www.udemy.com")
#         time.sleep(20)
#
#
if __name__ == "__main__":
    #ff = RunChromeTests_xyz()
    test_Udemy_Login_Method()
