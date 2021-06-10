import time
import unittest

from selenium.webdriver import Chrome

from liferay_automation.lib.liferay_forms_pages.home import LiferayFormsHomePage


class ActivityAuto1(unittest.TestCase):
    def setUp(self):
        webdriver = Chrome()
        url = "https://forms.liferay.com/web/forms/shared/-/form/122548"
        self.home = LiferayFormsHomePage(webdriver, url)

    def test_005(self):
        self.home.open()
        self.home.is_in_home_page()
        self.home.insert_name('Fernando Benbassat')
        self.home.insert_why_join_testing_area('Software testing is very cool.')
        self.home.submit_form()
        assert self.home.is_birth_field_required(), \
            '\'This field is required.\' text message was not found for \'What is the date of your birth?\''

    def tearDown(self):
        self.home.close()


if __name__ == "__main__":
    unittest.main()
