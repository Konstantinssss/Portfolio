
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement

class Tutu(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://www.tutu.ru/'
        super().__init__(driver, self.base_url)

        self.btn_burger_menu = WebElement(driver, 'span.richIcon_87ec6c5e.size_200_87ec6c5e.shapeNoShape_87ec6c5e > i')
        self.btn_main = WebElement(driver, 'div > a')