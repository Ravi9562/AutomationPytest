from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Add_Account:

    def __init__(self, driver):
        self.driver = driver

    def new_account(self):
        try:
            return self.driver.find_element_by_link_text('New Account')
        except:
            return None

    def wait_new_account(self):
        wait = WebDriverWait(driver=self.driver, timeout=30)
        wait.until(expected_conditions.visibility_of(self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/p')))

    def customer_id(self):
        try:
            return self.driver.find_element_by_name('cusid')
        except:
            return None

    def account_type(self):
        try:
            return self.driver.find_element_by_name('selaccount')
        except:
            return None

    def initial_deposit(self):
        try:
            return self.driver.find_element_by_name('inideposit')
        except:
            return None

    def Submit(self):
        try:
            return self.driver.find_element_by_name('button2')
        except:
            return None

    def Reset(self):
        try:
            return self.driver.find_element_by_name('reset')
        except:
            return None