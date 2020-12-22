from unittest import TestCase
import time

from lib.ui.Login_page import LoginPage
from lib.ui.add_customer import add_customer
from lib.utils import create_driver


class TestAddCustomer(TestCase):

    def setUp(self):
        self.driver = create_driver.browser_instance()
        self.login_page = LoginPage(self.driver)
        self.add_customer = add_customer(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_tc04(self):
        self.login_page.wait_login_page()
        self.login_page.username().send_keys('mngr280001')
        self.login_page.password().send_keys('uqytYgy')
        self.login_page.Login().click()
        self.add_customer.new_customer().click()
        self.add_customer.wait_for_new_customer_page()
        self.add_customer.customer_name().send_keys('sirendra')
        self.add_customer.gender_male().click()
        self.add_customer.dob().send_keys('05-11-2013')
        self.add_customer.address().send_keys('Jamnagar')
        self.add_customer.city().send_keys('Jamnagar')
        self.add_customer.state().send_keys('Gujarat')
        self.add_customer.pin().send_keys('567322')
        self.add_customer.mobile_no().send_keys('8000439025')
        self.add_customer.emailid().send_keys('Silverendra@gmail.com')
        self.add_customer.password().send_keys('67903')
        self.add_customer.submit().click()
        success = self.add_customer.registered_successfully().text
        expected_result = 'Customer Registered Successfully!!!'
        customer_id_text = self.add_customer.customer_id().text
        print(self.customer_id_text)
        assert success == expected_result
        self.add_customer.continue_button().click()
        time.sleep(6)
