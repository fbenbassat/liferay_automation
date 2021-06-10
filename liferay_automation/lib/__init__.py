from abc import ABC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PageElement(ABC):
    def __init__(self, webdriver, url=''):
        self.webdriver = webdriver
        self.url = url

    def open(self):
        self.webdriver.maximize_window()
        self.webdriver.get(self.url)

    def is_in_page(self, table_title, element):
        # Assert for page title
        assert table_title in self.webdriver.title, 'The page title on the browser tab is wrong.'
        # Wait page load
        WebDriverWait(self.webdriver, 15).until(lambda browser: self.webdriver.find_element_by_css_selector(element))

    def insert_text(self, element_xpath, text):
        field_element = WebDriverWait(self.webdriver, 10).until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
        field_element.clear()
        field_element.send_keys(text)

    def close(self):
        self.webdriver.close()
