
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement

class Tutu(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://www.tutu.ru/'
        super().__init__(driver, self.base_url)

        self.btn_burger_menu = WebElement(driver, 'span.richIcon_87ec6c5e.size_200_87ec6c5e.shapeNoShape_87ec6c5e > i')
        self.btn_main = WebElement(driver, 'div > a')
        self.mail_form = WebElement(driver, 'form > p')
        self.mail_field = WebElement(driver, 'form > div.M1GbbEXp9gG_S6hF > div > div > label > input')
        self.checkbox_agree_personal_data = WebElement(driver, 'div.vAimOUTZ4A35oNLK > label > span:nth-child(1)')
        self.btn_subscribe = WebElement(driver, 'div.M1GbbEXp9gG_S6hF > button')
        self.notice_incorrect_mail = WebElement(driver, 'div.M1GbbEXp9gG_S6hF > div > span')
        self.notice_correct_mail = WebElement(driver, 'div:nth-child(7) > div > div > div > div > div > div > p')
