import requests
import pytest
from hillel_api import s, auth, cars, expenses, users


# def test_signup_positive():
#     user_data= {
#         "name": "John",
#         "lastName": "Dou",
#         "email": "qam2808@2022test.com",
#         "password": "Qam2608venv",
#         "repeatPassword": "Qam2608venv"
#     }
#     r = auth.signup(s, user_data)
#     r_json = r.json()
#     assert r.status_code == 201, f"Wrong status code:\n{r_json}"
#     assert r_json.get('status', False) == "ok", "Key 'status' is not ok"
#
#
# def test_signin_positive():
#     user_data = {
#         "email": "qam2808@2022test.com",
#         "password": "Qam2608venv",
#         "remember": False
#     }
#     r = auth.signin(s, user_data)
#     r_json = r.json()
#     assert r.status_code == 200, f"Wrong status code:\n{r_json}"
#     assert r_json.get('status', False) == "ok", "Key 'status' is not ok"
#
# def get_a(a):
#     """Nazva testu"""
#     return int(a)
#
# def test_error():
#     with pytest.raises(
#          ValueError
#          ):
#         a ='dsdsd'
#         get_a(a)
#
#
# def get_error():
#     raise AttributeError("character name empty")
#
#
# def test_error_message():
#     with pytest.raises(
#             AttributeError,
#             match="character name empty"
#             ):
#         get_error()

# Homework
"""
https://qauto.forstudy.space/api-docs/
Написати п'ять тестів що проходять через пункти
1. Реєстрація користувача
2. Створення машини POST cars
3. редагування машини
4. отримання даних через GET в Cars або Expenses
5. Видалення користувача
"""




def test_signup_1():
    user_data= {
        "name": "Bill",
  "lastName": "Gates",
  "email": "testBill123@test.com",
  "password": "Qwerty123456",
  "repeatPassword": "Qwerty123456"
    }
    r = auth.signup(s, user_data)
    r_json = r.json()
    assert r.status_code == 201, f"Wrong status code:\n{r_json}"
    assert r_json.get('status', False) == "ok", "Key 'status' is not ok"


def test_signin_1():
    user_data = {
        "email": "testBill123@test.com",
        "password": "Qwerty123456",
        "remember": False
    }
    r = auth.signin(s, user_data)
    r_json = r.json()
    assert r.status_code == 200, f"Wrong status code:\n{r_json}"
    assert r_json.get('status', False) == "ok", "Key 'status' is not ok"


def test_cars_post_1():
    user_data = {
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 125
    }
    r = cars.cars_post(s, user_data)
    r_json = r.json()
    print(r_json)
    assert r.status_code == 201, f"Wrong status code:\n{r_json}"
    assert r_json.get('status', False) == "ok", "Key 'status' is not ok"
    print(r_json)


def test_cars_id_put_1():
    user_data = {
         "carBrandId": 1,
         "carModelId": 1,
         "mileage": 168225
    }
    r = cars.cars_id_put(s, user_data)
    r_json = r.json()
    # assert r.status_code == 200, f"Wrong status code:\n{r_json}"
    # assert r_json.get('status', False) == "ok", "Key 'status' is not ok"
    assert r.status_code == 404, f"Expected status code 404, but got {r.status_code}"
    assert r_json.get('status', '') == "error", "Expected 'status' to be 'error'"
    assert r_json.get('message', '') == "Car not found", "Expected 'message' to be 'Car not found'"


def test_expenses_get_1():
    r = expenses.expenses_get(s)
    r_json = r.json()
    assert r.status_code == 200, f"Wrong status code:\n{r_json}"
    assert r_json.get('status', False) == "ok", "Key 'status' is not ok"


def test_users_1():
        r = users.users(s)
        r_json = r.json()
        assert r.status_code == 200, f"Wrong status code:\n{r_json}"
        assert r_json.get('status', False) == "ok", "Key 'status' is not ok"
