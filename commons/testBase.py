__author__ = 'jgarcia'

from selenium import webdriver


class testBase():
    def __init__(self):
        self.driver = None

    def setUp(self):
        self.driver = webdriver.Firefox()


    def tearDown(self):
        self.driver.close()
