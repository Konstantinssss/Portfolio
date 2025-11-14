import time
from pages.base_page import BasePage
from pages.tutu import Tutu
from components.components import WebElement
import pytest

def test_tutu(browser):
    tutu_page = Tutu(browser)
    tutu_page.visit() # 1) Войти на сайт
    tutu_page.mail_form.scroll_to_element() # 2) Проскролить до формы подписки на рассылку
    # 3) Проверка валидации адреса электронной почты:
    tutu_page.mail_field.send_keys('mm.mail') # а) Ввод адреса почты без домена
    tutu_page.checkbox_agree_personal_data.click() # тап на чекбокс
    tutu_page.btn_subscribe.click() # тап на кнопку "Отправить"
    time.sleep(3)
    assert tutu_page.notice_incorrect_mail.exist() # увеломление о невалидном адресе почты

    tutu_page.mail_field.clear() # очистка формы заполнения адреса почты
    tutu_page.mail_field.send_keys('mmmail.ru') # б) Ввод почты без символа '@'
    tutu_page.btn_subscribe.click() # тап на кнопку "Отправить"
    time.sleep(3)
    assert tutu_page.notice_incorrect_mail.exist() # увеломление о невалидном адресе почты

    tutu_page.mail_field.clear() # очистка формы заполнения адреса почты
    tutu_page.mail_field.send_keys(' ') # в) Ввод пробела
    tutu_page.btn_subscribe.click() # тап на кнопку "Отправить"
    time.sleep(3)
    assert tutu_page.notice_incorrect_mail.exist() # увеломление о невалидном адресе почты

    tutu_page.mail_field.clear() # очистка формы заполнения адреса почты
    tutu_page.btn_subscribe.click() # г) тап на кнопку "Отправить" без заполнения формы адреса почты
    time.sleep(3)
    assert tutu_page.notice_incorrect_mail.exist() # увеломление о невалидном адресе почты
    assert tutu_page.notice_incorrect_mail.get_text() == 'Заполните обязательное поле'

    tutu_page.mail_field.send_keys('mm@mail.ru') # д) Ввод валидного адреса почты
    tutu_page.btn_subscribe.click() # тап на кнопку "Отправить"
    time.sleep(3)
    assert tutu_page.notice_correct_mail.exist() # проверка страницы happy end