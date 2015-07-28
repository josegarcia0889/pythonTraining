__author__ = 'jgarcia'


def open_logOn_Screen(self):
        assert self.driver.find_element_by_id("logindisplay").is_displayed()

        elem = self.driver.find_element_by_xpath(".//*[@id='logindisplay']/a")

        elem.click()

        assert self.driver.find_element_by_id("login-account").is_displayed()