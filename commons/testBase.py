__author__ = 'jgarcia'
import unittest
from selenium import webdriver

class testBase(unittest.TestCase):

  def setUp(self):
        self.driver = webdriver.Firefox()

  def tearDown(self):
     self.driver.close()
