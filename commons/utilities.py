__author__ = 'jgarcia'

from pythonTraining.commons.testBase import testBase


class utilities(testBase):


    def __init__(self):
        pass

    def homePage(self):
        driver = self.setUp

        self.driver.get("http://nerddinner.com")

        self.assertIn("Nerd Dinner", driver.title)

        driver.maximize_window()

        assert "No results found." not in driver.page_source
