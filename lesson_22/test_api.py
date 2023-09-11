"""HomeTask_22.

https://qauto.forstudy.space/api-docs/
Написати п'ять тестів що проходять через пункти
1. Реєстрація користувача
2. Створення машини POST cars
3. редагування машини
4. отримання даних через GET в Cars або Expenses
5. Видалення користувача
"""

import pytest
from hillel_api import s, auth, users, cars


@pytest.fixture
def create_user():
    """Create user function."""
    user_data = {
        'name': 'Education',
        'lastName': 'Hillel',
        'email': 'EducationHillel3@2023test.com',
        'password': 'Qwerty@123456',
        'repeatPassword': 'Qwerty@123456',
    }
    r = auth.signup(s, user_data)
    r_json = r.json()
    assert r.status_code == 201, f'Wrong status code:\n{r_json}'
    return r_json


def test_signup_positive(create_user):
    """test_signup_positive function."""
    r_json = create_user
    assert r_json.get('status', False) == 'ok', "Key 'status' is not ok"


def test_signin_positive():
    """test_signin_positive function."""
    user_data = {
        'email': 'EducationHillel3@2023test.com',
        'password': 'Qwerty@123456',
        'remember': False,
    }
    r = auth.signin(s, user_data)
    r_json = r.json()
    assert r.status_code == 200, f'Wrong status code:\n{r_json}'
    assert r_json.get('status', False) == 'ok', "Key 'status' is not ok"


@pytest.fixture
def create_car():
    """create_car function."""
    user_data = {
        'carBrandId': 1,
        'carModelId': 1,
        'mileage': 99,
    }
    r = cars.cars_post(s, user_data)
    r_json = r.json()
    assert r.status_code == 201, f'Wrong status code:\n{r_json}'
    return r_json


def test_create_car_positive(create_car):
    """test_create_car_positive function."""
    r_json = create_car
    assert r_json.get('status', False) == 'ok', "Key 'status' is not ok"


@pytest.fixture
def response_id(create_car):
    """response_id function."""
    return create_car.get('data').get('id')


def test_cars_edit_positive(response_id):
    """test_cars_edit_positive function."""
    user_data = {
        'id': response_id,
        'carBrandId': 2,
        'carModelId': 2,
        'mileage': 101,
    }
    r = cars.cars_id_put(s, user_data)
    r_json = r.json()
    assert r.status_code == 200, f'Wrong status code:\n{r_json}'
    assert r_json.get('status', False) == 'ok', "Key 'status' is not ok"


def test_get_data_in_cars_positive(response_id):
    """test_get_data_in_cars_positive function."""
    r = cars.cars_get(s, response_id)
    r_json = r.json()
    assert r.status_code == 200, f'Wrong status code:\n{r_json}'
    assert r_json.get('status', False) == 'ok', "Key 'status' is not ok"


def test_delete_user_positive():
    """test_delete_user_positive function."""
    r = users.users(s)
    r_json = r.json()
    assert r.status_code == 200, f'Wrong status code:\n{r_json}'
    assert r_json.get('status', False) == 'ok', "Key 'status' is not ok"
