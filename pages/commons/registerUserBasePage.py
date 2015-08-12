__author__ = 'jgarcia'


class RegisterUserBasePage(object):
    def __init__(self):
        self.driver = None

    def loadDriver(self,driver2):
        self.driver = driver2

    def open_register_screen(self):
        assert self.driver.find_element_by_css_selector("div[id=login-account]>form>div>p>a").is_displayed()

        self.driver.find_element_by_css_selector("div[id=login-account]>form>div>p>a").click()

        assert self.driver.title == ("Register for an account")

        assert self.driver.find_element_by_id("UserName").is_displayed()
        assert self.driver.find_element_by_id("Email").is_displayed()
        assert self.driver.find_element_by_id("Password").is_displayed()
        assert self.driver.find_element_by_id("ConfirmPassword").is_displayed()

    def registerForm_fillIn(self, username, email, password):
        self.driver.find_element_by_id("UserName").send_keys(username)
        self.driver.find_element_by_id("Email").send_keys(email)
        self.driver.find_element_by_id("Password").send_keys(password)
        self.driver.find_element_by_id("ConfirmPassword").send_keys(password)

    def click_registerButton(self):
        assert self.driver.find_element_by_css_selector(
            "div[id='main']>form>div>fieldset>p>input[type='submit']").is_displayed()
        self.driver.find_element_by_css_selector("div[id='main']>form>div>fieldset>p>input[type='submit']").click()
