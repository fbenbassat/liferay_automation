from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from liferay_automation.lib import PageElement


class InformationSentPage(PageElement):
    xpath_title = "//h1[@class='ddm-form-name'][contains(text(), 'Information sent')]"
    xpath_description = "//*[@class='ddm-form-description'][contains(text(), 'Information sent successfully!')]"

    def is_in_information_page(self):
        try:
            # Wait page load
            WebDriverWait(self.webdriver, 20).until(lambda browser: self.webdriver.find_element_by_xpath(
                self.xpath_title))
            WebDriverWait(self.webdriver, 20).until(lambda browser: self.webdriver.find_element_by_xpath(
                self.xpath_description))
            return True
        except TimeoutException:
            return False


