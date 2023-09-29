from selenium.webdriver.common.by import By

from hillel_aqa_050623.lesson_27.locators.base_locators import BaseLocators


class MainPageLocators(BaseLocators):
    GUEST_LOGIN = (By.XPATH, '//button[@class="header-link -guest"]')
    SIGN_IN_BTN = (By.XPATH, '//button[@class="btn btn-outline-white header_signin"]')
    CONTACT_BTN = (By.XPATH, '//button[contains(text(), "Contacts")]')
    CONTACTS = (By.CLASS_NAME, 'socials_link')

    # LOGIN FORM
    EMAIL_INPUT = (By.XPATH, '//*[@id="signinEmail"]')
    PASS_INPUT = (By.ID, 'signinPassword')
    LOGIN_BTN = (By.XPATH, '//button[@class="btn btn-primary"]')
    RESTORE_PASS = (By.CSS_SELECTOR, '.form-group .btn.btn-link')
    ALERT_MESSAGE = (By.CSS_SELECTOR, '.alert.alert-success')

    # LOGGED USER
    LOG_OUT = (By.XPATH, '//span[@class="icon icon-logout"]')
    CARS = (By.CLASS_NAME, 'car-item')
    ADD_CAR = (By.XPATH, '//button[@class="btn btn-primary" and contains(text(), "Add")]')
    CAR_BRAND_SELECTOR = (By.XPATH, '//select[@name="carBrandId"]')
    CAR_BRAND_SELECTOR_OPTION = (By.XPATH, '//*[@id="addCarBrand"]/option')
    CAR_MODEL_SELECTOR = (By.XPATH, '//select[@id="addCarModel"]')
    CAR_MODEL_SELECTOR_OPTION = (By.XPATH, '//*[@id="addCarModel"]/option')
    CAR_MILES = (By.XPATH, '//input[@id="addCarMileage"]')
    UPDATE_CAR_MILES_INPUT = (By.CLASS_NAME, 'update-mileage-form_input')
    UPDATE_CAR_MILES_BTN = (By.CLASS_NAME, 'update-mileage-form_submit')
    EDIT_CAT_BTN = (By.XPATH, '//button[@class="car_edit btn btn-edit"]')
    DELETE_CAR_BTN = (By.XPATH, '//button[@class="btn btn-outline-danger"]')
    CONFIRM_DELETE_CAR_BTN = (By.CSS_SELECTOR, '.modal-content .btn.btn-danger')
    HEADER_LOGO = (By.CLASS_NAME, 'header_logo')