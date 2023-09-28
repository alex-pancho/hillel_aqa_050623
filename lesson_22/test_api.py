import pytest
from hillel_api import s, auth, cars, expenses, users
"""
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

https://qauto.forstudy.space/api-docs/
Написати п'ять тестів що проходять через пункти
1. Реєстрація користувача
2. Створення машини POST cars
3. редагування машини
4. отримання даних через GET в Cars або Expenses
5. Видалення користувача
"""


def test_auth_signup_positive():
    """
    Test of API functionality of user signup
    """
    user_data = {
        "name": "John",
        "lastName": "Dou",
        "email": "1122334455@test.com",
        "password": "Qam2608venv",
        "repeatPassword": "Qam2608venv"
    }
    r = auth.signup(s, user_data)
    r_json = r.json()
    assert r.status_code == 201, f"Wrong status code:\n{r_json}"
    assert r_json.get('status', False) == "ok", "Key 'status' is not ok"


car_id = None


def test_cars_post_positive():
    """
    Test of API functionality of car creation
    """
    cars_data = {
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 1222
    }
    global car_id
    r = cars.cars_post(s, cars_data)
    r_json = r.json()
    car_id = r_json.get('data', {}).get('id')
    assert r.status_code == 201, f"Wrong status code:\n{r_json}"
    assert r_json.get('status', False) == "ok", "Key 'status' is not ok"


def test_cars_put_positive():
    """
    Test of API functionality of updating car information
    """
    global car_id
    if car_id is None:
        pytest.fail("No car_id available. Please run test_cars_post_positive first.")

    updated_cars_data = {
        "id": car_id,
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 168223,
    }
    r = cars.cars_id_put(s, updated_cars_data)
    r_json = r.json()
    assert r.status_code == 200, f"Wrong status code:\n{r_json}"
    assert r_json.get('status', False) == "ok", "Key 'status' is not ok"


def test_expenses_get_positive():
    """
    Test of API functionality of receiving car's data
    """
    car_id = test_cars_put_positive()
    request_body = {
        "id": car_id,
        "page": 0
    }
    r = expenses.expenses_get(s, request_body)
    r_json = r.json()
    assert r.status_code == 200, f"Wrong status code:\n{r_json}"
    assert r_json.get('status', False) == "ok", "Key 'status' is not ok"


def test_user_delete_positive():
    """
    Test of API functionality of deleting user's data
    """
    r = users.users(s)
    r_json = r.json()
    assert r.status_code != 200, f"Wrong status code:\n{r_json}"
    assert r_json.get('status', False) == "ok", "Key 'status' is not ok"
