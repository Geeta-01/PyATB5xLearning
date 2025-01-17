from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os


@allure.title("Demo ESPOCRM positive Testcase")
@allure.description("TC1 - Positive TC - Verify the Title and current URL.")
@pytest.mark.Positive
def test_Verify_Title_chrome():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("URL_DemoESPO"))
    #print(driver.title)
    assert driver.title=="EspoCRM Demo"
    assert driver.current_url=="https://demo.us.espocrm.com/"

    driver.quit()  # close everything.