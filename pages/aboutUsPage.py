__author__ = 'jgarcia'

from pythonTraining.pages.commons.aboutUsBasePage import AboutUsBasePage
from pythonTraining.commons.testBase import Base
from pythonTraining.commons.utilities import Utilities


class AboutUsPage(AboutUsBasePage):
    def __init__(self):
        self.utilities = Utilities()

        self.driver = None

    def verify_aboutUs_displayed(self):
        self.driver = Base().setUp()

        self.utilities.home_page(self.driver)
        self.click_tab(2)
        self.verify_aboutUs_screenDisplayed()

        Base().tearDown(self.driver)
