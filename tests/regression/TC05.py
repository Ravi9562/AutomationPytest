from unittest import TestCase
import time

from lib.ui.Login_page import LoginPage
from lib.ui.add_account import Add_Account
from lib.utils import create_driver
from tests.regression.TC04 import TestAddCustomer


class TestAddAccount(TestCase):
    def setUp(self):
        self.driver = create_driver.browser_instance()
        self.login_page = LoginPage(self.driver)
        self.add_account = Add_Account(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_tc05(self):
        self.login_page.wait_login_page()
        self.login_page.username().send_keys('mngr280000')
        self.login_page.password().send_keys('uqytYgy')
        self.login_page.Login().click()
        self.add_account.new_account().click()
        self.add_account.wait_new_account()
        cid_text = TestAddCustomer.customer_id_text
        self.add_account.customer_id().send_keys(cid_text)
        time.sleep(5)
