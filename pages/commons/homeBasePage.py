__author__ = 'jgarcia'

import pythonTraining.commons.properties as property
from unittestzero import Assert


class HomeBasePage(object):
    def __init__(self):
        self.driver = object

    def load_driver(self, driver2):  # This method works when user calls methods in this class from an external source
        self.driver = driver2

    def compare_images(self):
        assert self.driver.find_element_by_css_selector("nav").is_displayed()

        icons = self.driver.find_elements_by_css_selector("img[src^='/Content/Img/icon']")

        Assert.equal(icons.__len__(), 3)
        Assert.equal(icons[0].get_attribute("src"), property.oDataFeed)
        Assert.equal(icons[1].get_attribute("src"), property.rss)
        Assert.equal(icons[2].get_attribute("src"), property.calfeed)







