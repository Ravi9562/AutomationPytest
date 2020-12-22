from unittest import TestCase
import time

from lib.ui.Login_page import LoginPage
from lib.utils import create_driver
from lib.utils.create_driver import browser_instance

class TestLoginSuccess(TestCase):

    def setUp(self):
        self.driver = create_driver.browser_instance()
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_LoginSuccess(self):
        self.login_page.wait_login_page()
        self.login_page.username().send_keys('mngr280000')
        self.login_page.password().send_keys('uqytYgy')
        self.login_page.Login().click()
        self.login_page.loginsuccessfully()

    def test_pagetitle(self):
        self.login_page.wait_login_page()
        self.login_page.username().send_keys('mngr280000')
        self.login_page.password().send_keys('uqytYgy')
        self.login_page.Login().click()
        self.login_page.loginsuccessfully()
        homepage_title = self.driver.title
        expected_title = "Guru99 Bank Manager HomePage"
        assert  homepage_title == expected_title