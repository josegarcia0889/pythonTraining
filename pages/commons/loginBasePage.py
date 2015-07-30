__author__ = 'jgarcia'



class LogInBasePage():
    def __init__(self):
        self.driver = None

    def open_logOn_Screen(self, driver2):

        self.driver = driver2

        assert self.driver.find_element_by_id("logindisplay").is_displayed()

        elem = self.driver.find_element_by_xpath(".//*[@id='logindisplay']/a")

        elem.click()

        assert self.driver.find_element_by_id("login-account").is_displayed()