import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/'



def test_store(browser, language):
    browser.get(link+language+'/catalogue/coders-at-work_207/')
    browser.find_element(By.CSS_SELECTOR, 'button.btn[value]').click()
    assert browser.find_element(By.CSS_SELECTOR, 'div.alertinner'), 'Error'

