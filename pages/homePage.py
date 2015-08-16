__author__ = 'jgarcia'

from pythonTraining.pages.commons.homeBasePage import HomeBasePage
from pythonTraining.commons.testBase import Base
from pythonTraining.commons.utilities import Utilities


class HomePage(HomeBasePage):
    def __init__(self):
        self.utilities = Utilities()

        self.driver = None

    def compare_img_url(self):
        self.driver = Base().setUp()

        self.utilities.home_page(self.driver)
        self.compare_images()

        Base().tearDown(self.driver)

