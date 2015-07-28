__author__ = 'jgarcia'

from pythonTraining.commons.testBase import testBase


class Utilities(testBase):

    def home_page(self):
        driver = self.setUp

        self.driver.get("http://nerddinner.com", self)

        self.assertIn("Nerd Dinner", driver.title)

        driver.maximize_window()

        assert "No results found." not in driver.page_source
