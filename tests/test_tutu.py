import time
from pages.base_page import BasePage
from pages.tutu import Tutu
from components.components import WebElement
import pytest

@pytest.mark.my_marker
def test_tutu(browser):
    tutu_page = Tutu(browser)
    tutu_page.visit()
    time.sleep(5)
    tutu_page.btn_burger_menu.click()