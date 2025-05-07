import pytest
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button_displays(browser):
    browser.get(URL)

    try:
        add_to_basket_btn = browser.find_element(
            By.CSS_SELECTOR,
            "button.btn.btn-lg.btn-primary.btn-add-to-basket"
        )
    except NoSuchElementException:
        assert False, "Add to basket button not found"