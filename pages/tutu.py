
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement

class Tutu(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://www.tutu.ru/'
        super().__init__(driver, self.base_url)

        self.btn_burger_menu = WebElement(driver, '#__next > header > div > div > ul > li.listStyleTypeNone_2c663590.marginRight450_36bb7eca > ul > li:nth-child(1) > a')
        self.btn_main = WebElement(driver, 'div > a')