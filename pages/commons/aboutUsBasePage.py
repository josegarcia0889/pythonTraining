__author__ = 'jgarcia'


class AboutUsBasePage(object):
    def __init__(self):
        self.driver = object

    def loadDriver(self,driver2):
        self.driver = driver2

    def click_aboutUs_tab(self):
        assert self.driver.find_element_by_css_selector("a[href='/Home/About']").is_displayed()

        elem = self.driver.find_element_by_css_selector("a[href='/Home/About']")

        elem.click()


    def verify_aboutUs_screenDisplayed(self):
        assert "No results found." not in self.driver.page_source

        assert self.driver.find_element_by_id("about").is_displayed()