import os

import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException
import utilities.CustomLogger as log
import time

from traceback import print_stack
from appium.webdriver.common.appiumby import AppiumBy

waitTime = 10
BASE_DIR = os.getcwd()
logger = log.custom_logger()

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        
    def save_screen_shot_tofile(self):
         image_file_name = f'{time.strftime("%Y%m%d_%H%M%S")}_.png'
         image_file_path = os.path.join(BASE_DIR + "/reports", image_file_name)
         self.driver.save_screenshot(image_file_path)
         logger.info(f'{image_file_path} saved')


    def take_screenshotoallure(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

    def is_displayed(self, locator):
        self.driver.implicitly_wait(waitTime)
        try:
            self.driver.find_element(by=AppiumBy.XPATH, value=locator).is_displayed()
            self.take_screenshotoallure(locator)
            logger.info("Displayed locator value " + locator)
            return True
        except NoSuchElementException:
            print_stack()
            logger.info("No Displayed locator value " + locator)
            self.take_screenshotoallure(locator)
            self.save_screen_shot_tofile()
            return False
    
    def click_elements_by_xpath(self, locator):
        self.driver.implicitly_wait(waitTime)
        try:
            el = self.driver.find_element(by=AppiumBy.XPATH, value=locator)
            self.take_screenshotoallure(locator)
            el.click()
        except NoSuchElementException:
            print_stack()
            logger.info(
                "Unable to Click with locator value " + locator)
            self.take_screenshotoallure(locator)
            self.save_screen_shot_tofile()
            assert False
