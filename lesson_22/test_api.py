import json

import requests
import pytest
from hillel_api import s, auth, cars, users


def test_signup_positive():
    user_data= {
        "name": "John",
        "lastName": "Dou",
        "email": "qam2808@2022test.com",
        "password": "Qam2608venv",
        "repeatPassword": "Qam2608venv"
    }
    r = auth.signup(s, user_data)
    r_json = r.json()
    assert r.status_code == 201, f"Wrong status code:\n{r_json}"
    assert r_json.get('status', False) == "ok", "Key 'status' is not ok"


def test_signin_positive():
    user_data = {
        "email": "qam2808@2022test.com",
        "password": "Qam2608venv",
        "remember": False
    }
    r = auth.signin(s, user_data)
    r_json = r.json()
    assert r.status_code == 200, f"Wrong status code:\n{r_json}"
    assert r_json.get('status', False) == "ok", "Key 'status' is not ok"

def get_a(a):
    """Nazva testu"""
    return int(a)

def test_error():
    with pytest.raises(
         ValueError
         ):
        a ='dsdsd'
        get_a(a)


def get_error():
    raise AttributeError("character name empty")


def test_error_message():
    with pytest.raises(
            AttributeError,
            match="character name empty"
            ):
        get_error()

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

def  test_signup_user():
    user_1={
        "name": "Aksana",
        "lastName": "Kandr",
        "email": "ak345@2022test.com",
        "password": "Qam2608venv",
        "repeatPassword": "Qam2608venv"

    }
    r = auth.signup(s, user_1)
    r_json = r.json()
    assert r.status_code == 201, f"Wrong status code:\n{r_json}"
    assert r_json.get('status', False) == "ok", "Key 'status' is not ok"



def  test_signin_user():
        user_data = {
            "email": "ak345@2022test.com",
            "password": "Qam2608venv",
            "remember": False
        }
        r = auth.signin(s, user_data)
        r_json = r.json()
        user_id=r_json['data']['userId']
        assert r.status_code == 200, f"Wrong status code"
        assert isinstance(user_id, int) and 10000 <= user_id <= 99999, 'Wrong userID'
        j_str = json.dumps(r_json)
        print(j_str)

def test_create_a_car():

    user_data={
        "email": "ak345@2022test.com",
        "password":"Qam2608venv",
    }

    auth.signin(s,user_data)

    car_data={

        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 122
    }
    r=cars.cars_post(s, car_data)
    r_json=r.json()
    assert r.status_code==201, f"Wrong status code:\n{r_json}"
    assert r_json.get('status', False) == "ok", "Key 'status' is not ok"



def test_update_car():
    user_data = {
        "email": "ak345@2022test.com",
        "password": "Qam2608venv",
    }
    auth.signin(s, user_data)
    car_data={

            "userId": 48463,
            "carBrandId": 1,
            "carModelId": 1,
            "mileage": 220
        }
    r=cars.cars_id_put(s, car_data)
    r_json=r.json()
    assert r.status_code == 200, f"Wrong status code"
    assert r_json.get('status', False) == "ok", "Key 'status' is not ok"


def test_get_car_data():
    user_data = {
        "email": "ak345@2022test.com",
        "password": "Qam2608venv",
    }
    auth.signin(s, user_data)
    r = cars.cars_get(s,user_data)
    r_json=r.json()
    assert r.status_code == 200, f"Wrong status code"
    assert r_json.get('status', False) == "ok", "Key 'status' is not ok"


def test_delete_user():
    user_data = {
        "email": "ak345@2022test.com",
        "password": "Qam2608venv",
    }

    auth.signin(s, user_data)
    r=users.users(s,user_data)
    r_json=r.json()
    assert r.status_code == 200, f"Wrong status code"
    assert r_json.get('status', False) == "ok", "Key 'status' is not ok"





