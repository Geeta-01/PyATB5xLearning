import allure
import pytest
import requests

@allure.title("Verify the GET request of Restful Booker")
@allure.description("This testcase checks for Booking 1 and verify the response")
def test_GetRequest_Positive():
    #print("Create booking positive TC")
    get_url ="https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url = get_url)
    print(response_data.text)
    assert response_data.status_code == 200

@allure.title("Verify the GET request of Restful Booker with invalid data")
@allure.description("This testcase checks for Booking -1 and verify the response")
def test_GetRequest_negative():
    get_url ="https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url = get_url)
    print(response_data.text)
    assert response_data.status_code == 404
