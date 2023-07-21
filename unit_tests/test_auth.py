import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from for_test_auth import login, password

logins = [
    pytest.param(
        "super_user@m", "olala",
        marks=pytest.mark.xfail,
        id='wrong login'
    ),
    pytest.param(
        login, "olala",
        marks=pytest.mark.xfail,
        id='wrong password'
    ),
    pytest.param(
        login, password,
        id='correct login and password'
    )
]


@pytest.mark.parametrize('login, password', logins)
def test_auth(login, password):
    driver = webdriver.Chrome()
    driver.get('https://passport.yandex.ru/auth')
    element1 = driver.find_element(By.XPATH, "//button[@data-type='login']")
    element1.click()
    element2 = driver.find_element(By.XPATH, "//input[@id='passp-field-login']")
    time.sleep(2)
    element2.send_keys(login)
    element2.send_keys(Keys.ENTER)
    time.sleep(2)
    input_password_correct = driver.find_element(By.ID, "passp-field-passwd")
    time.sleep(2)
    input_password_correct.clear()
    input_password_correct.send_keys(password)
    input_password_correct.send_keys(Keys.ENTER)
    time.sleep(2)
    result = driver.current_url
    driver.close()
    assert result == 'https://id.yandex.ru/'
