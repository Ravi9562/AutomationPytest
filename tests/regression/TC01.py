from unittest import TestCase

from lib.ui.Login_page import LoginPage
from lib.ui.Homepage import Homepage
from lib.utils import create_driver


class TestLogintest(TestCase):
    def setUp(self):
        self.driver = create_driver.browser_instance()
        self.login_page = LoginPage(self.driver)
        self.homepage = Homepage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_tc01(self):
        self.login_page.wait_login_page()
        self.login_page.username().send_keys('mngr280000')
        self.login_page.password().send_keys('uqytYgy')
        self.login_page.Login().click()
        self.homepage.Changepassword().click()
        self.homepage.OldPassword().send_keys('uqytYgs')
        self.homepage.NewPassword().send_keys('123456')
        self.homepage.ConfirmPassword().send_keys('123456')
        self.homepage.Submit().click()
        pop_up = self.driver.switch_to.alert
        content = pop_up.text
        pop_up.accept()
        expected_content = "Old Password is incorrect"
        assert expected_content == content
