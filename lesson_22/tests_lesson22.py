import requests
import pytest
from hillel_api import s, auth, cars, users


# Homework for lesson 22
"""
https://qauto.forstudy.space/api-docs/
Написати п'ять тестів що проходять через пункти
1. Реєстрація користувача
2. Створення машини POST cars
3. редагування машини
4. отримання даних через GET в Cars або Expenses
5. Видалення користувача
"""


# Test for creating a car
def test_signup_positive():
    user_data= {
        "name": "Joddhn",
        "lastName": "Doddu",
        "email": "qamqq2808@2022test.com",
        "password": "Qam2608venv",
        "repeatPassword": "Qam2608venv"
    }
    r = auth.signup(s, user_data)
    r_json = r.json()
    assert r.status_code == 201, f"Wrong status code:\n{r_json}"
    assert r_json.get('status', False) == "ok", "Key 'status' is not ok"


# Sign in
def test_signin_positive():
    user_data = {
        "email": "qamqq2808@2022test.com",
        "password": "Qam2608venv",
        "remember": False
    }
    r = auth.signin(s, user_data)
    r_json = r.json()
    assert r.status_code == 200, f"Wrong status code:\n{r_json}"
    assert r_json.get('status', False) == "ok", "Key 'status' is not ok"


# Test for creating a car
def test_create_car():
    # Authenticate the user first
    user_data = {
        "email": "qamqq2808@2022test.com",
        "password": "Qam2608venv"
    }
    auth.signin(s, user_data)

    # Create a car
    car_data = {
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 122,
    }
    response = cars.cars_post(s, car_data)
    response_json = response.json()
    assert response.status_code == 201, f"Wrong status code:\n{response_json}"
    assert response_json.get('status', False) == "ok", "Key 'status' is not ok"


# Test for editing a car
def test_edit_car():
    # Authenticate the user first
    user_data = {
        "email": "qamqq2808@2022test.com",
        "password": "Qam2608venv"
    }
    auth.signin(s, user_data)

    # Edit the car
    car_data = {
        "id": 55580,
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 168223
    }
    response = cars.cars_id_put(s, car_data)
    response_json = response.json()
    assert response.status_code == 200, f"Wrong status code:\n{response_json}"
    assert response_json.get('status', False) == "ok", "Key 'status' is not ok"

# Test for getting data via GET in Cars or Expenses
def test_get_cars():
    # Authenticate the user first
    user_data = {
        "email": "qamqq2808@2022test.com",
        "password": "Qam2608venv"
    }
    auth.signin(s, user_data)

    # Now, you can proceed to retrieve cars
    response = cars.cars_get(s)
    response_json = response.json()

    # Assert the status code is 200 (OK)
    assert response.status_code == 200, f"Wrong status code:\n{response_json}"

    # Assert that the 'status' key in the response is 'ok'
    assert response_json.get('status', False) == "ok", "Key 'status' is not ok"

    # Assert that the 'data' field in the response contains a list of cars
    cars_list = response_json.get('data', [])
    assert isinstance(cars_list, list) and len(cars_list) > 0, "No cars data found"

    # Assert the structure of the first car in the list
    first_car = cars_list[0]
    assert 'id' in first_car, "Car ID is missing"
    assert 'brand' in first_car, "Car brand is missing"  # Adjust to 'brand' field
    assert 'logo' in first_car, "Car logo is missing"

# Test for deleting a user
def test_delete_user():

    # Authenticate the user first
    user_data = {
        "email": "qamqq2808@2022test.com",
        "password": "Qam2608venv"
    }
    auth.signin(s, user_data)

    # Delete user
    response = users.users(s)
    response_json = response.json()
    assert response.status_code == 200, f"Wrong status code:\n{response_json}"
    assert response_json.get('status', False) == "ok", "Key 'status' is not ok"
