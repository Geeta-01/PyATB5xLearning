from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os


@allure.title("Demo ESPOCRM Positive Testcase")
@allure.description("TC4 - Positive TC - Click on Sales pack link ")
@pytest.mark.Positive
def test_click_SalesPack_chrome():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.get(os.getenv("URL_DemoESPO"))
    time.sleep(5)
    sales_pack_link_element = driver.find_element(By.XPATH, "//a[@href='https://www.espocrm.com/extensions/sales-pack/']")
    sales_pack_link_element.click()
    time.sleep(10)

    driver.quit()  # close everything.