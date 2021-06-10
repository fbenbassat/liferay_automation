from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from liferay_automation.lib import PageElement


class LiferayFormsHomePage(PageElement):
    tab_title = 'This is a Liferay Forms'
    btn_submit = (By.ID, 'ddm-form-submit')
    css_name_field = '.ddm-field[data-field-name="WhatIsYourName"]'
    xpath_name_text = "//div[@data-field-name='WhatIsYourName']/div/input"
    xpath_why_join_testing_area = "//div[@data-field-name='WhyDidYouJoinTheTestingArea']/div/textarea"
    xpath_birth_field_date = "//*[@class='date-picker']//*/input[@type='text']"
    xpath_birth_field_required_text = "//div[@data-field-name='WhatIsTheDateOfYourBirth']/div/span/div"

    def submit_form(self):
        self.webdriver.find_element(By.ID, 'ddm-form-submit').click()

    def is_in_home_page(self):
        self.is_in_page(self.tab_title, self.css_name_field)

    def insert_name(self, name):
        self.insert_text(self.xpath_name_text, name)

    def insert_why_join_testing_area(self, text):
        self.insert_text(self.xpath_why_join_testing_area, text)

    def insert_date_birth(self, date):
        self.insert_text(self.xpath_birth_field_date, date)

    def is_birth_field_required(self):
        field_element = WebDriverWait(self.webdriver, 15).until(lambda browser: self.webdriver.find_element(
            By.XPATH, self.xpath_birth_field_required_text))
        element_color = field_element.value_of_css_property('color')
        # Verify text and color red.
        return field_element.text == 'This field is required.' and element_color == 'rgba(218, 20, 20, 1)'


