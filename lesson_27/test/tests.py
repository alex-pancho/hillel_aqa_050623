import random
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions

from lesson_27.locators.qauto_page_locators import MainPageLocators
from lesson_27.test.conftest import USERNAME, PASSWORD, URL, USER_DATA


# 1
def test_login_as_guest(open_students_site):
    # USE FIXTURE FOR OPENING THE PAGE AND INITIALIZED DRIVER
    driver, page = open_students_site

    # CLICK GUEST LOGIN
    driver.find_element(MainPageLocators.GUEST_LOGIN.by, MainPageLocators.GUEST_LOGIN.locator).click()

    try:
        WebDriverWait(driver, 10).until(
            EC.url_contains('/panel/garage')
        )
    except Exception:
        print(f'URL is not correct, received: {driver.current_url}')
    try:
        logout_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[@class="btn btn-link '
                                                      'text-danger btn-sidebar sidebar_btn"]'))
        )
        logout_button.click()
    except Exception:
        print(f'Unable to locate LOG OUT button')


# 2
def test_login_as_exist_user(open_students_site):
    # USE FIXTURE FOR OPENING THE PAGE AND INITIALIZED DRIVER
    driver, page = open_students_site

    # CLICK SIGN IN LOGIN
    driver.find_element(MainPageLocators.SIGN_IN_BTN.by, MainPageLocators.SIGN_IN_BTN.locator).click()

    # FILL SIGN IN FORM
    page.login_as_user(*USER_DATA)

    # CHECK URL
    try:
        assert page.wait.until(expected_conditions.url_contains('/panel/garage'))
    except Exception:
        print(f'URL is not correct, received: {driver.current_url}')
    # LOGOUT
    driver.find_element(MainPageLocators.LOG_OUT.by, MainPageLocators.LOG_OUT.locator).click()
    driver.find_element(MainPageLocators.HEADER_LOGO.by, MainPageLocators.HEADER_LOGO.locator).click()


# 3
def test_check_contacts(open_students_site):
    # USE FIXTURE FOR OPENING THE PAGE AND INITIALIZED DRIVER
    driver, page = open_students_site

    # CLICK CONTACTS
    driver.find_element(MainPageLocators.CONTACT_BTN.by, MainPageLocators.CONTACT_BTN.locator).click()

    # ASSERT
    social_links = driver.find_elements(MainPageLocators.CONTACTS.by, MainPageLocators.CONTACTS.locator)
    assert len(social_links) == 5, f'Expected 5 social links, received {len(social_links)}'
    # Assert that the href attribute contains 'hillel'
    expected_substring = 'hillel'
    for link in social_links:
        # Get the href attribute value
        href_attribute = link.get_attribute('href').lower()
        assert expected_substring in href_attribute, f"Expected '{expected_substring}' in href: {href_attribute}"

        # Additional assert that link is clickable
        page.wait.until(EC.element_to_be_clickable(link))


# 4
def test_logout(open_students_site):
    # USE FIXTURE FOR OPENING THE PAGE AND INITIALIZED DRIVER
    driver, page = open_students_site

    # LOGIN AS GUEST
    driver.find_element(MainPageLocators.GUEST_LOGIN.by, MainPageLocators.GUEST_LOGIN.locator).click()

    # LOGOUT
    driver.find_element(MainPageLocators.LOG_OUT.by, MainPageLocators.LOG_OUT.locator).click()

    # CHECK URL
    try:
        assert page.wait.until(expected_conditions.url_to_be(f'https://{USERNAME}:{PASSWORD}@{URL}/'))
    except Exception as e:
        print(f"  URL is wrong, URL  {driver.current_url}")


# 5
def test_add_car(open_as_logged_user):
    # USE FIXTURE FOR OPENING THE PAGE AND INITIALIZED DRIVER
    driver, page = open_as_logged_user

    # Get CARS amount before update
    cars_amount = len(driver.find_elements(
        MainPageLocators.CARS.by, MainPageLocators.CARS.locator))

    # ADD CAR
    page.add_car()

    # Get CARS amount after update
    cars_amount_new = len(page.wait.until(EC.presence_of_all_elements_located
                                          ((MainPageLocators.CARS.by, MainPageLocators.CARS.locator))))
    assert cars_amount_new > cars_amount, f'Cars amount is not increased'
    driver.find_element(MainPageLocators.HEADER_LOGO.by, MainPageLocators.HEADER_LOGO.locator).click()


# 6
def test_update_car_mileage(open_as_logged_user):
    # USE FIXTURE FOR OPENING THE PAGE AND INITIALIZED DRIVER
    driver, page = open_as_logged_user

    # Get CARS amount before update
    cars_amount = len(page.wait.until(EC.presence_of_all_elements_located(
        (MainPageLocators.CARS.by, MainPageLocators.CARS.locator))))
    if cars_amount == 0:
        pytest.skip('No cars to update')
    # print(cars_amount)

    # UPDATE CAR MILES
    new_miles = str(random.randint(2222, 9999))
    page.update_car_mileage(new_miles)
    driver.find_element(MainPageLocators.HEADER_LOGO.by, MainPageLocators.HEADER_LOGO.locator).click()


# 7
def test_delete_all_cars(open_as_logged_user):
    # USE FIXTURE FOR OPENING THE PAGE AND INITIALIZED DRIVER
    driver, page = open_as_logged_user

    # Get CARS amount before update
    cars_amount = len(page.wait.until(EC.presence_of_all_elements_located(
        (MainPageLocators.CARS.by, MainPageLocators.CARS.locator))))
    if cars_amount == 0:
        pytest.skip('No cars to delete')
    # print(cars_amount)

    # DELETE ALL CARS
    page.delete_all_cars(cars_amount)
    log_out_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((MainPageLocators.HEADER_LOGO.by, MainPageLocators.HEADER_LOGO.locator))
    )
    log_out_element.click()
    # driver.find_element(MainPageLocators.HEADER_LOGO.by, MainPageLocators.HEADER_LOGO.locator).click()
    # LOGOUT
    driver.find_element(MainPageLocators.LOG_OUT.by, MainPageLocators.LOG_OUT.locator).click()
