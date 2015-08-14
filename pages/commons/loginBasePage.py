__author__ = 'jgarcia'


class LogInBasePage(object):
    def __init__(self):
        self.driver = object

    def load_driver(self,driver2):  # This method works when user calls methods in this class from an external source
        self.driver = driver2

    def open_logOn_Screen(self):
        assert self.driver.find_element_by_id("logindisplay").is_displayed()

        elem = self.driver.find_element_by_css_selector("div[id='logindisplay']>a")

        elem.click()

        assert self.driver.find_element_by_id("login-account").is_displayed()

    def click_logOn_button(self):
        logonButton = self.driver.find_element_by_class_name("classiclogon")

        logonButton.click()

    def validate_required_fields(self):
        userNameField = self.driver.find_element_by_id("UserName")
        passwordField = self.driver.find_element_by_id("Password")

        errorText = self.driver.find_elements_by_class_name("field-validation-error")

        assert userNameField.get_attribute("class") == ("input-validation-error")
        assert errorText[0].text == ("The Username: field is required.")

        assert passwordField.get_attribute("class") == ("input-validation-error")
        assert errorText[1].text == ("The Password: field is required.")

    def write_username_password(self, user, passw):
        self.driver.find_element_by_id("UserName").is_displayed()
        self.driver.find_element_by_id("Password").is_displayed()

        self.driver.find_element_by_id("UserName").send_keys(user)
        self.driver.find_element_by_id("Password").send_keys(passw)

    def validate_wrong_username_password(self):
        assert self.driver.find_element_by_class_name("validation-summary-errors").is_displayed()
        assert self.driver.find_element_by_class_name("validation-summary-errors").text == (
            "Login was unsuccessful. Please correct the errors and try again.\nThe user name or password provided is incorrect.")
        assert self.driver.find_element_by_class_name("field-validation-error").text == (
            "The username or password provided is incorrect.")

    def verify_logged_user(self, username):
        assert self.driver.find_element_by_id("logindisplay").is_displayed()
        assert self.driver.find_element_by_id("logindisplay").text == ("Welcome " + username + "! [ Log Off ]")


