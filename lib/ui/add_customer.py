from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class add_customer:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_new_customer_page(self):
        wait = WebDriverWait(driver=self.driver, timeout=30)
        wait.until(expected_conditions.visibility_of(self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/p')))

    def new_customer(self):
        try:
            return self.driver.find_element_by_link_text('New Customer')
        except:
            return None

    def customer_name(self):
        try:
            return self.driver.find_element_by_name('name')
        except:
            return None

    def gender_male(self):
        try:
            return self.driver.find_element_by_name('rad1')
        except:
            return None

    def gender_female(self):
        try:
            return self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[2]')
        except:
            return None

    def dob(self):
        try:
            return self.driver.find_element_by_id('dob')
        except:
            return None

    def address(self):
        try:
            return self.driver.find_element_by_name('addr')
        except:
            return None

    def city(self):
        try:
            return self.driver.find_element_by_name('city')
        except:
            return None
        
    def state(self):
        try:
            return self.driver.find_element_by_name('state')
        except:
            return None

    def pin(self):
        try:
            return self.driver.find_element_by_name('pinno')
        except:
            return None

    def mobile_no(self):
        try:
            return self.driver.find_element_by_name('telephoneno')
        except:
            return None

    def emailid(self):
        try:
            return self.driver.find_element_by_name('emailid')
        except:
            return None

    def password(self):
        try:
            return self.driver.find_element_by_name('password')
        except:
            return None

    def submit(self):
        try:
            return self.driver.find_element_by_name('sub')
        except:
            return None

    def reset(self):
        try:
            return self.driver.find_element_by_name('res')
        except:
            return None
    def registered_successfully(self):
        try:
            return self.driver.find_element_by_xpath('//*[@id="customer"]/tbody/tr[1]/td/p')
        except:
            return None

    def continue_button(self):
        try:
            return self.driver.find_element_by_link_text('Continue')
        except:
            return None
    def customer_id(self):
        try:
            return self.driver.find_element_by_xpath('//*[@id="customer"]/tbody/tr[4]/td[2]')
        except:
            return None