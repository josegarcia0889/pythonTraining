__author__ = 'jgarcia'
import unittest
from random import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def openPage(self):
        driver = self.driver
        driver.get("http://nerddinner.com")

        self.assertIn("Nerd Dinner", driver.title)

        driver.maximize_window()

        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()


    def open_logOn_Screen(self):
        assert self.driver.find_element_by_id("logindisplay").is_displayed()

        elem = self.driver.find_element_by_xpath(".//*[@id='logindisplay']/a")

        elem.click()

        assert self.driver.find_element_by_id("login-account").is_displayed()


    def open_Register_Screen(self):
        assert self.driver.find_element_by_xpath(".//*[@id='login-account']/form/div/p[5]/a").is_displayed()

        self.driver.find_element_by_xpath(".//*[@id='login-account']/form/div/p[5]/a").click()

        assert self.driver.title == ("Register for an account")

        assert self.driver.find_element_by_id("UserName").is_displayed()
        assert self.driver.find_element_by_id("Email").is_displayed()
        assert self.driver.find_element_by_id("Password").is_displayed()
        assert self.driver.find_element_by_id("ConfirmPassword").is_displayed()



    def open_RegisterForm_FillIn(self,username,email,password):

        self.driver.find_element_by_id("UserName").send_keys(username)
        self.driver.find_element_by_id("Email").send_keys(email)
        self.driver.find_element_by_id("Password").send_keys(password)
        self.driver.find_element_by_id("ConfirmPassword").send_keys(password)


    def click_RegisterButton(self):
        assert self.driver.find_element_by_xpath(".//*[@id='main']/form/div/fieldset/p[5]/input").is_displayed()
        self.driver.find_element_by_xpath(".//*[@id='main']/form/div/fieldset/p[5]/input").click()


    def verify_logged_user(self,username):
        assert self.driver.find_element_by_id("logindisplay").is_displayed()
        assert self.driver.find_element_by_id("logindisplay").text == ("Welcome " + username +"! [ Log Off ]")




#------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------


        # TEST 1
    def test_login_requiredFields(self):
        self.openPage()

        self.open_logOn_Screen()

        logonButton = self.driver.find_element_by_class_name("classiclogon")

        logonButton.click()

        userNameField = self.driver.find_element_by_id("UserName")
        passwordField = self.driver.find_element_by_id("Password")

        errorText = self.driver.find_elements_by_class_name("field-validation-error")

        assert userNameField.get_attribute("class") == ("input-validation-error")
        assert errorText[0].text == ("The Username: field is required.")

        assert passwordField.get_attribute("class") == ("input-validation-error")
        assert errorText[1].text == ("The Password: field is required.")

        self.tearDown()


         # TEST 2
    def test_login_wrongUsername_Password(self):
        self.openPage()

        self.open_logOn_Screen()

        self.driver.find_element_by_id("UserName").send_keys("testUSer")
        self.driver.find_element_by_id("Password").send_keys("123456789")

        self.driver.find_element_by_class_name("classiclogon").click()

        assert self.driver.find_element_by_class_name("validation-summary-errors").is_displayed()
        assert self.driver.find_element_by_class_name("validation-summary-errors").text == ("Login was unsuccessful. Please correct the errors and try again.\nThe user name or password provided is incorrect.")
        assert self.driver.find_element_by_class_name("field-validation-error").text == ("The username or password provided is incorrect.")
        self.tearDown()


         # TEST 3
    def test_RegisterScreenDisplayed(self):
        self.openPage()

        self.open_logOn_Screen()

        self.open_Register_Screen()

        self.tearDown()



         # TEST 4
    def test_Successfully_RegisterUser(self):
        self.openPage()

        self.open_logOn_Screen()

        self.open_Register_Screen()

        username ="jgarcia"+str(random())

        self.open_RegisterForm_FillIn(username,"jgarcia+"+str(random())+"@wearegap.com","123456")

        self.click_RegisterButton()

        self.verify_logged_user(username)

        self.tearDown()

