r"""HomeTask_28.

Наша команда має завдання написати тести, що перевірятимуть наявність
 та працезданість всіх єлементів сторінки https://qauto.forstudy.space/

Потрібно взяти  і використовуючи патерн PageObjects написати 10 тестів,
що перевірять:

Хоча б один елемент головного меню
Форму логіна - її заповнення та, власне, логін
Меню, що доступне зареестрованому користовачу
Додавання машини в гараж для зареєстрованого користувача
Наявність контактів з компанією на головній сторінці
"""


from hometask_28 import get_login_button, get_email_input, get_password_input
from hometask_28 import get_about_button, click, get_sign_in_button, get_hillel
from hometask_28 import get_brand_car_button, get_model_car_button
from hometask_28 import get_select_model_car_button, get_mileage_button, get_add_button
from hometask_28 import get_mileage_update_button, get_mileage_update_value, get_save_button
from hometask_28 import get_add_expensetotalcost, get_add_fuel_expense, get_remove_car
from hometask_28 import get_dropdown_my_profile_button, get_dropdown_logout_button
from hometask_28 import get_dropdown_garage_button, get_mail_button, insert_text
from hometask_28 import get_add_car_button, get_select_brand_car_button, get_edit_button
from hometask_28 import get_add_expenseliters, get_remove_button, get_add_fuelexpense_button
from time import sleep

driver = get_hillel()


def test_about_button():
    """test_about_button function."""
    about_btn = get_about_button(driver)
    click(about_btn)


def test_login():
    """test_login function."""
    email = 'shavlak1939@gmail.com'
    password = 'Qwerty@12345'
    sign_in_btn = get_sign_in_button(driver)
    click(sign_in_btn)
    email_input = get_email_input(driver)
    password_input = get_password_input(driver)
    insert_text(email_input, email)
    insert_text(password_input, password)
    log_btn = get_login_button(driver)
    click(log_btn)
    sleep(5)


def test_add_car_1():
    """test_add_car_1 function."""
    car = 'BMW'
    model = 'Z3'
    mileage = 100
    add_car_btn = get_add_car_button(driver)
    sleep(2)
    click(add_car_btn)
    brand_car_btn = get_brand_car_button(driver)
    sleep(2)
    click(brand_car_btn)
    select_brand_car_btn = get_select_brand_car_button(driver, car)
    sleep(2)
    click(select_brand_car_btn)
    model_car_btn = get_model_car_button(driver)
    sleep(2)
    click(model_car_btn)
    select_model_car_btn = get_select_model_car_button(driver, model)
    sleep(2)
    click(select_model_car_btn)
    mileage_input = get_mileage_button(driver)
    add_btn = get_add_button(driver)
    insert_text(mileage_input, mileage)
    sleep(2)
    click(add_btn)
    sleep(2)


def test_add_car_2():
    """test_add_car_2 function."""
    car = 'Audi'
    model = 'A8'
    mileage = 120
    add_car_btn = get_add_car_button(driver)
    sleep(2)
    click(add_car_btn)
    brand_car_btn = get_brand_car_button(driver)
    sleep(2)
    click(brand_car_btn)
    select_brand_car_btn = get_select_brand_car_button(driver, car)
    sleep(2)
    click(select_brand_car_btn)
    model_car_btn = get_model_car_button(driver)
    sleep(2)
    click(model_car_btn)
    select_model_car_btn = get_select_model_car_button(driver, model)
    sleep(2)
    click(select_model_car_btn)
    mileage_input = get_mileage_button(driver)
    add_btn = get_add_button(driver)
    insert_text(mileage_input, mileage)
    sleep(2)
    click(add_btn)


def test_update_mileage_car():
    """test_update_mileage_car function."""
    mileage_new = 1111
    add_mileage_update_button = get_mileage_update_button(driver)
    add_mileage_value = get_mileage_update_value(driver)
    sleep(2)
    click(add_mileage_value)
    add_mileage_value.clear()
    sleep(2)
    insert_text(add_mileage_value, mileage_new)
    sleep(2)
    click(add_mileage_update_button)


def test_edit_car():
    """test_edit_car function."""
    car = 'Ford'
    model = 'Sierra'
    mileage = 1112
    edit_car_btn = get_edit_button(driver)
    sleep(2)
    click(edit_car_btn)
    brand_car_btn = get_brand_car_button(driver)
    sleep(2)
    click(brand_car_btn)
    select_brand_car_btn = get_select_brand_car_button(driver, car)
    sleep(2)
    click(select_brand_car_btn)
    model_car_btn = get_model_car_button(driver)
    sleep(2)
    click(model_car_btn)
    select_model_car_btn = get_select_model_car_button(driver, model)
    sleep(2)
    click(select_model_car_btn)
    mileage_input = get_mileage_button(driver)
    save_btn = get_save_button(driver)
    click(mileage_input)
    mileage_input.clear()
    insert_text(mileage_input, mileage)
    sleep(2)
    click(save_btn)
    sleep(2)


def test_add_fuel_expense_car():
    """test_add_fuel_expense_car function."""
    number_of_litres = 10
    total_cost = 15000
    add_fuel_expense_button = get_add_fuel_expense(driver)
    click(add_fuel_expense_button)
    number_of_litres_button = get_add_expenseliters(driver)
    total_cost_button = get_add_expensetotalcost(driver)
    click(number_of_litres_button)
    insert_text(number_of_litres_button, number_of_litres)
    sleep(2)
    click(total_cost_button)
    insert_text(total_cost_button, total_cost)
    sleep(2)
    add_button = get_add_fuelexpense_button(driver)
    click(add_button)
    sleep(2)


def test_remove_cars():
    """test_remove_car function."""
    profile_button = get_dropdown_my_profile_button(driver)
    click(profile_button)
    sleep(2)
    garage_button = get_dropdown_garage_button(driver)
    click(garage_button)
    sleep(2)
    edit_car_btn = get_edit_button(driver)
    click(edit_car_btn)
    sleep(2)
    remove_car_button = get_remove_car(driver)
    click(remove_car_button)
    sleep(2)
    remove_button = get_remove_button(driver)
    click(remove_button)
    sleep(2)
    edit_car_btn = get_edit_button(driver)
    click(edit_car_btn)
    sleep(2)
    remove_car_button = get_remove_car(driver)
    click(remove_car_button)
    sleep(2)
    remove_button = get_remove_button(driver)
    click(remove_button)
    sleep(2)


def test_logout_button():
    """test_logout_button function."""
    my_profile_button = get_dropdown_my_profile_button(driver)
    click(my_profile_button)
    sleep(1)
    logout_button = get_dropdown_logout_button(driver)
    click(logout_button)
    sleep(1)


def test_mail():
    """test_mail function."""
    mail = 'developer@ithillel.ua'
    contact_element = get_mail_button(driver)
    contact_href = contact_element.get_attribute('href')
    if mail in contact_href:
        click(contact_element)
    else:
        print('E-mail is not found')
