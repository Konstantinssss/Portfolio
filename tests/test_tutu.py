import time
from pages.base_page import BasePage
from pages.tutu import Tutu
from components.components import WebElement
import pytest

@pytest.mark.my_marker
def test_tutu(browser):
    tutu_page = Tutu(browser)
    tutu_page.visit()
    tutu_page.mail_form.scroll_to_element()

    tutu_page.mail_field.send_keys('mm.mail')
    tutu_page.checkbox_agree_personal_data.click()
    tutu_page.btn_subscribe.click()
    time.sleep(3)
    assert tutu_page.notice_incorrect_mail.exist()

    tutu_page.mail_field.clear()
    tutu_page.mail_field.send_keys('mmmail.ru')
    tutu_page.btn_subscribe.click()
    time.sleep(3)
    assert tutu_page.notice_incorrect_mail.exist()

    tutu_page.mail_field.clear()
    tutu_page.mail_field.send_keys(' ')
    tutu_page.btn_subscribe.click()
    time.sleep(3)
    assert tutu_page.notice_incorrect_mail.exist()

    tutu_page.mail_field.clear()
    tutu_page.btn_subscribe.click()
    time.sleep(3)
    assert tutu_page.notice_incorrect_mail.exist()
    assert tutu_page.notice_incorrect_mail.get_text() == 'Заполните обязательное поле'

    tutu_page.mail_field.send_keys('mm@mail.ru')
    tutu_page.btn_subscribe.click()
    time.sleep(3)
    assert tutu_page.notice_correct_mail.exist()
