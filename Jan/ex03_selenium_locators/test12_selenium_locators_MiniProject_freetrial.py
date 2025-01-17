from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
from dotenv import load_dotenv

@allure.title("VWO Positive Testcase")
@allure.description("TC1 - Click on Start a free trial link and verify the URL of next page")
@pytest.mark.positiveTC
def test_app_vwo_startTrial_chrome():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("URL"))
    #Find the element
    #locator for web element "Free Trial"
    #< a
    #href = "https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage"

    #class ="text-link" data-qa="bericafeqo" >
    # Start a free trial
    #< / a >
    startTrial_webelement_locator = driver.find_element(By.LINK_TEXT, "Start a free trial")
    startTrial_webelement_locator.click()
    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"

    time.sleep(5)
    driver.quit()  # close everything.