__author__ = 'jgarcia'


class AboutUsBasePage(object):
    def __init__(self):
        self.driver = object

    def load_driver(self, driver2):  # This method works when user calls methods in this class from an external source
        self.driver = driver2

    # def click_aboutUs_tab(self):
    #      assert self.driver.find_element_by_css_selector("a[href='/Home/About']").is_displayed()
    #     elem = self.driver.find_element_by_css_selector("a[href='/Home/About']")
    #    elem.click()

    def click_aboutUs_tab(self):
        assert self.driver.find_element_by_id("menu").is_displayed()

        elem_menu = self.driver.find_element_by_id("menu")

        elem_menu.find_element_by_css_selector("[href='/Home/About']").click()

    #  img[src^='/Content/Img/icon']
    def verify_aboutUs_screenDisplayed(self):
        assert "No results found." not in self.driver.page_source

        assert self.driver.find_element_by_id("about").is_displayed()