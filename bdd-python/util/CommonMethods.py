import random
import time

from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    StaleElementReferenceException
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from util.logger_util import get_logger

logger = get_logger(__name__)

class CommonMethods():

    def __init__(self, driver):
        self.driver = driver

    def wait(self, delay):
        return WebDriverWait(self.driver, delay)

    def open_url(self, url):
        logger.info(f"Open url: {url}")
        self.driver.get(url)
        self.driver.maximize_window()
        return self

    def wait_for_element_visible(self, locator, delay=10):
        logger.info(
            "Wait for element visible - " + str(locator) + " delay:" + str(delay)
        )
        self.wait(delay).until(EC.visibility_of_element_located(locator))
        return self

    def wait_for_elements_visible(self, locator, delay=10):
        logger.info(
            "Wait for elements visible - " + str(locator) + " delay:" + str(delay)
        )
        self.wait(delay).until(EC.visibility_of_all_elements_located(locator))
        return self

    def wait_until_element_not_visible(self, locator, delay=10):
        logger.info(
            "Wait until element not visible - " + str(locator) + " delay:" + str(delay)
        )
        self.wait(delay).until(EC.invisibility_of_element_located(locator))
        return self

    def get_text(self, locator, delay=10):
        if delay != 0:
            try:
                self.wait_for_element_visible(locator, delay)
            except:
                self.wait_for_element_presence(locator, delay)
        text = self.driver.find_element(*locator).text
        logger.info("Get text - " + str(locator) + " text:" + str(text))
        return text

    def get_texts(self, locator, delay=10):
        txt_list = []
        if delay != 0:
            self.wait_for_element_visible(locator, delay)
        text = self.driver.find_elements(*locator)
        for i in text:
            logger.info(i.text)
            txt_list.append(i.text)
        logger.info("Get text - " + str(locator) + " text:" + str(txt_list))
        return txt_list

    def random_picker(self, list):
        item = random.choice(list)  # Chooses from list
        logger.info(f"Item picked randomly = '{item}' from list = {list}")
        return item

    def wait_for_element_clickable(self, locator, delay=10):
        logger.info(
            "Wait for element clickable - " + str(locator) + " delay:" + str(delay)
        )
        self.wait(delay).until(EC.element_to_be_clickable(locator))
        return self

    def wait_for_element_presence(self, locator, delay=10):
        logger.info(
            "Wait for element presence - " + str(locator) + " delay:" + str(delay)
        )
        self.wait(delay).until(EC.presence_of_element_located(locator))
        return self

    def click_element(self, locator, delay=10):
        logger.info("Click element - " + str(locator))
        self.wait(delay).until(EC.element_to_be_clickable(locator)).click()
        return self

    def get_elements(self, locator, delay=0):
        elements = []
        try:
            if delay != 0:
                self.wait_for_elements_visible(locator, delay)
            elements = self.driver.find_elements(*locator)
        except (
                StaleElementReferenceException,
                TimeoutException,
                NoSuchElementException,
        ):
            logger.info("Element not present - " + str(locator))
        logger.info(f"Elements = {len(elements)}")
        return elements

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        logger.info("Get text -> " + str(text))
        time.sleep(1)
        alert.accept()
        return text

    def refresh_page(self):
        self.driver.refresh()
