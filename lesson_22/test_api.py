import requests
import pytest
import json
import re

from hillel_api import s, auth, cars, users

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

# def get_a(a):
#     """Nazva testu"""
#     return int(a)

# def test_error():
#     with pytest.raises(
#          ValueError
#          ):
#         a ='dsdsd'
#         get_a(a)


# def get_error():
#     raise AttributeError("character name empty")


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

def test_auth_getID():
    """Проверяем что значение user_id в респонсе это интеджер состоящий из 5 символов"""
    user_data = {
    "email": "test0909@test.com",
    "password": "Qwerty12345"
    }
    r = auth.signin(s, user_data)
    response_data = r.json()  # Преобразование JSON-ответа в словарь
    user_id = response_data['data']['userId']  # Извлечение значения 'userId'
    assert r.status_code == 200, 'Wrong status code'
    assert isinstance(user_id, int) and 10000 <= user_id <= 99999, 'userId should be 5 digits integer'
    json_str = json.dumps(response_data, indent=4)  # indent=4 добавляет отступы для красивого форматирования
    # Выводим JSON-строку в консоли
    print(json_str)


@pytest.mark.skip
def test_cars_post():
    """Проверяем что респонс возвращает 201 статус код"""
    user_data = {
    "carBrandId": 1,
    "carModelId": 1,
    "mileage": 122
    }
    r = cars.cars_post(s, user_data)
    assert r.status_code == 201, 'Wrong status code'
    response_data = r.json()
    json_str = json.dumps(response_data, indent=4)  # indent=4 добавляет отступы для красивого форматирования
    # Выводим JSON-строку в консоли
    print(json_str)


def test_cars_id_put():
    """Проверяем что респонс возвращает обновленное значение "mileage"""
    user_data = {
    "id": 54455,
    "carBrandId": 1,
    "carModelId": 1,
    "mileage": 222
    }
    r = cars.cars_id_put(s, user_data)
    assert r.status_code == 200, 'Wrong status code'
    response_data = r.json()
    updated_mileage = response_data['data']['mileage']  # Извлечение значения 'mileage'
    assert user_data["mileage"] == updated_mileage, "Wrong the updated mileage"
    json_str = json.dumps(response_data, indent=4)  # indent=4 добавляет отступы для красивого форматирования
    # Выводим JSON-строку в консоли
    print(json_str)

def test_cars_get_brands():
    """Проверка что название файла логотипа соответствует марке автомобиля"""
    r = cars.brands(s)
    assert r.status_code == 200, 'Wrong status code'
    response_data = r.json()
    json_str = json.dumps(response_data, indent=4)  # indent=4 добавляет отступы для красивого форматирования
    # Выводим JSON-строку в консоли
    print(json_str)
    for item in response_data['data']:
        title_value = item['title']
        logo_filename = item['logoFilename']
        # Преобразуем title_value в нижний регистр и убираем расширение .png в logo_filename
        title_normalized = title_value.lower()
        logo_normalized = re.sub(r'\.png$', '', logo_filename)
        # Проверяем что название файла png содержит соответствующее наименование марки автомобиля
        assert logo_normalized == title_normalized, f"Logo filename '{logo_filename}' does not match title '{title_value}'"

@pytest.mark.skip
def test_users_delete():
    """Проверяем что респонс возвращает 200 статус код"""
    r = users.users(s)
    assert r.status_code == 200, 'Wrong status code'
    response_data = r.json()
    json_str = json.dumps(response_data, indent=4)  # indent=4 добавляет отступы для красивого форматирования
    # Выводим JSON-строку в консоли
    print(json_str)

