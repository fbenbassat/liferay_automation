import unittest

from selenium.webdriver import Chrome

from liferay_automation.lib.liferay_forms_pages.confirmation import InformationSentPage
from liferay_automation.lib.liferay_forms_pages.home import LiferayFormsHomePage


class ActivityAuto2(unittest.TestCase):
    def setUp(self):
        webdriver = Chrome()
        url = "https://forms.liferay.com/web/forms/shared/-/form/122548"
        self.home = LiferayFormsHomePage(webdriver, url)
        self.confirmation = InformationSentPage(webdriver)

    def test_017(self):
        self.home.open()
        self.home.is_in_home_page()
        self.home.insert_name('Fernando Benbassat')
        self.home.insert_why_join_testing_area('Software testing is very cool.')
        self.home.insert_date_birth('11/11/1122')
        self.home.submit_form()
        assert not self.confirmation.is_in_information_page(), 'Form was sent with invalid date birth.'
        assert self.home.is_invalid_data(), \
            'The error message with \'Invalid data for date birth\' is not found.'

    def tearDown(self):
        self.home.close()


if __name__ == "__main__":
    unittest.main()
