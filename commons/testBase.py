__author__ = 'jgarcia'

from selenium import webdriver


class Base():
    def __init__(self):
        pass

    def setUp(self):
        self.driver = webdriver.Firefox()  # Browser driver is set

        return self.driver

    def tearDown(self, driver2):  # Driver is closed after a test is finished
        self.driver = driver2
        self.driver.close()