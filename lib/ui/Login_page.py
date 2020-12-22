from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def wait_login_page(self):
        wait = WebDriverWait(driver=self.driver, timeout=30)
        wait.until(expected_conditions.visibility_of(self.username()))
        wait.until(expected_conditions.visibility_of(self.password()))

    def username(self):
        try:
            return self.driver.find_element_by_name('uid')
        except:
            return None

    def password(self):
        try:
            return self.driver.find_element_by_name('password')
        except:
            return None

    def Login(self):
        try:
            return self.driver.find_element_by_name('btnLogin')
        except:
            return None

    def Reset(self):
        try:
            return self.driver.find_element_by_name('btnReset')
        except:
            return None

    def loginsuccessfully(self):
        try:
            return self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/marquee')
        except:
            return None
