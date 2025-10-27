
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement

class Tutu(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://www.tutu.ru/'
        super().__init__(driver, self.base_url)