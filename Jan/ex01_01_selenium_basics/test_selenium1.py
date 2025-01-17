import time

from selenium import webdriver
import allure
import pytest


@allure.title("Open the app.vwo.com")
@pytest.mark.regresssion
def test_vwo_login():
    driver = webdriver.Edge()
    driver.get("https:/app.vwo.com")
    driver.maximize_window()
    time.sleep(2)
    driver.close()