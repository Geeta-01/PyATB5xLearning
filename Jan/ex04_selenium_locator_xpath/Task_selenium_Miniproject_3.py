# Automation for the Registration Page of the AwesomeQA.com/UI
#     Open - https://awesomeqa.com/ui/index.php?route=account/register
#     Fill the form
#     Verify that next page give - Your Account Has Been Created!
#------------------------------------------------------
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@allure.title("Selenium Mini project- Locator-XPATH #3")
@allure.description("TC1 - Positive TC - Fill the registration form with valid data and verify whether account created ")
@pytest.mark.Positive
def test_fill_reg_form():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    time.sleep(5)
    ele_firstname = driver.find_element(By.XPATH,"//input[@id='input-firstname']")
    ele_lastname =driver.find_element(By.XPATH,"//input[@id='input-lastname']")
    ele_email = driver.find_element(By.XPATH,"//input[@id='input-email']")
    ele_phone = driver.find_element(By.XPATH,"//input[@id='input-telephone']")
    ele_password = driver.find_element(By.XPATH,"//input[@id='input-password']")
    ele_confirmPwd = driver.find_element(By.XPATH,"//input[@id='input-confirm']")
    ele_policy_checkbox =driver.find_element(By.XPATH, "//input[@name='agree']")
    ele_continue= driver.find_element(By.XPATH,"//*[@id='content']/form/div/div/input[2]")

    ele_firstname.send_keys("sample")
    ele_lastname.send_keys("example")
    ele_email.send_keys("sample_ex12@gmail.com")
    ele_phone.send_keys("1234567890")
    ele_password.send_keys("pass@1234")
    ele_confirmPwd.send_keys("pass@1234")
    ele_policy_checkbox.click()
    ele_continue.click()
    time.sleep(5)
    assert driver.current_url=="https://awesomeqa.com/ui/index.php?route=account/success"
    print(driver.title)
    time.sleep(10)
    driver.close()
