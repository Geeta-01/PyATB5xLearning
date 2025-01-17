from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os


@allure.title("Demo ESPOCRM Positive Testcase")
@allure.description("TC2 - Positive TC - Click on login and verify the current page Url")
@pytest.mark.Positive
def test_Verify_login_chrome():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.get(os.getenv("URL_DemoESPO"))
    time.sleep(5)
    login_button_element = driver.find_element(By.XPATH,"//button[@id='btn-login']")
    login_button_element.click()
    time.sleep(5)
    assert driver.current_url== os.getenv("URL_DemoESPO_Login")

    driver.quit()  # close everything.