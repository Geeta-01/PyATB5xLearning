import allure
import pytest

@allure.title("Verify the create booking with valid data")
@allure.description("This testcase checks for create booking positive scenario with valid data")
def test_positiveTC():
    print("Create booking positive TC")
    assert 1-1 == 2
@allure.title("Verify the create booking with invalid data")
@allure.description("This testcase checks for create booking negative scenario with invalid data")
def test_negativeTC1():
    print("Create booking negative TC1")
    assert 1+1 == 2

@allure.title("Verify the create booking with invalid data")
@allure.description("This testcase checks for create booking negative scenario with invalid data")
def test_negativeTC2():
    print("Create booking negative TC2")
    assert 1+1 == 2