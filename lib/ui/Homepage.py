from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Homepage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_homepage(self):
        wait = WebDriverWait(driver=self.driver, timeout=30)
        wait.until(expected_conditions.visibility_of(self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[3]/td')))

    def Changepassword(self):
        try:
            return self.driver.find_element_by_xpath('/html/body/div[3]/div/ul/li[11]/a')
        except:
            return None

    def OldPassword(self):
        try:
            return self.driver.find_element_by_name('oldpassword')
        except:
            return None

    def NewPassword(self):
        try:
            return self.driver.find_element_by_name('newpassword')
        except:
            return None

    def ConfirmPassword(self):
        try:
            return self.driver.find_element_by_name('confirmpassword')
        except:
            return None

    def Submit(self):
        try:
            return self.driver.find_element_by_name('sub')
        except:
            return None

    def Reset(self):
        try:
            return self.driver.find_element_by_name('res')
        except:
            return None