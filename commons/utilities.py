__author__ = 'jgarcia'

class utilities(object):

  def HomePage(self):
        driver = self.driver
        driver.get("http://nerddinner.com")

        self.assertIn("Nerd Dinner", driver.title)

        driver.maximize_window()

        assert "No results found." not in driver.page_source
