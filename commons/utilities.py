__author__ = 'jgarcia'

from pythonTraining.commons.testBase import testBase


class Utilities(testBase):

    def home_page(self):
        driver = testBase.setUp(self)

        self.driver.get("http://nerddinner.com")


        driver.assertIn("Nerd Dinner", driver.title)

        self.driver.assertIn("Nerd Dinner", driver.title)

        driver.maximize_window()

        assert "No results found." not in driver.page_source
