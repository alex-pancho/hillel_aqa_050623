import random
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from lesson_27.locators.qauto_page_locators import MainPageLocators


class BasePage:
    def __init__(self):
        """
        Initialize a new instance of BasePage with a WebDriver, ActionChains, and WebDriverWait.
        """
        self.__web_driver = webdriver.Chrome()
        self.__action = ActionChains(self.__web_driver)
        self.__wait = WebDriverWait(self.__web_driver, 15)

    @property
    def web_driver(self):
        """
        Get the WebDriver instance.
        """
        return self.__web_driver

    @property
    def action(self):
        """
        Get the ActionChains instance for performing user actions.
        """
        return self.__action

    @property
    def wait(self):
        """
        Get the WebDriverWait instance for waiting for elements to appear.
        """
        return self.__wait

    def login_as_user(self, email, password):
        """
        Log in as a user with the provided email and password.

        :param email: The user's email.
        :param password: The user's password.
        """
        # Fill email input
        self.web_driver.find_element(MainPageLocators.EMAIL_INPUT.by,
                                     MainPageLocators.EMAIL_INPUT.locator). \
            send_keys(email)

        # Fill email input
        self.web_driver.find_element(MainPageLocators.PASS_INPUT.by,
                                     MainPageLocators.PASS_INPUT.locator). \
            send_keys(password)

        # Click Login button
        self.web_driver.find_element(MainPageLocators.LOGIN_BTN.by,
                                     MainPageLocators.LOGIN_BTN.locator).click()

    def add_car(self):
        """
        Add a new car by selecting a brand, model, and entering the miles.
        """
        self.__wait.until(
            EC.element_to_be_clickable((MainPageLocators.ADD_CAR.by,
                                        MainPageLocators.ADD_CAR.locator))
        ).click()

        # Click on the add car brand selector
        self.__wait.until(
            EC.element_to_be_clickable((MainPageLocators.CAR_BRAND_SELECTOR.by,
                                        MainPageLocators.CAR_BRAND_SELECTOR.locator))
        ).click()
        car_options = self.web_driver.find_elements(MainPageLocators.CAR_BRAND_SELECTOR_OPTION.by,
                                                    MainPageLocators.CAR_BRAND_SELECTOR_OPTION.locator)
        random_car = random.randint(0, len(car_options) - 1)
        selected_brand = car_options[random_car].text
        car_options[random_car].click()

        # Click on the add car model selector
        self.__wait.until(
            EC.element_to_be_clickable((MainPageLocators.CAR_MODEL_SELECTOR.by,
                                        MainPageLocators.CAR_MODEL_SELECTOR.locator))
        ).click()
        options = self.web_driver.find_elements(MainPageLocators.CAR_MODEL_SELECTOR_OPTION.by,
                                                MainPageLocators.CAR_MODEL_SELECTOR_OPTION.locator)
        random_car_model = random.randint(0, len(options) - 1)
        selected_model = options[random_car_model].text
        options[random_car_model].click()

        # Enter the car miles
        miles = str(random.randint(2222, 9999))
        self.web_driver.find_element(MainPageLocators.CAR_MILES.by,
                                     MainPageLocators.CAR_MILES.locator).send_keys(miles)

        # Click save car
        self.web_driver.find_elements(MainPageLocators.ADD_CAR.by,
                                      MainPageLocators.ADD_CAR.locator)[-1].click()

    def update_car_mileage(self, new_miles):
        """
        Update the miles of a car with the provided new mileage.

        :param new_miles: The new mileage value.
        """
        miles = self.web_driver.find_elements(MainPageLocators.UPDATE_CAR_MILES_INPUT.by,
                                              MainPageLocators.UPDATE_CAR_MILES_INPUT.locator)[0]
        miles.clear()
        miles.send_keys(new_miles)

        # Click update button
        self.web_driver.find_elements(MainPageLocators.UPDATE_CAR_MILES_BTN.by,
                                      MainPageLocators.UPDATE_CAR_MILES_BTN.locator)[0].click()

    def delete_all_cars(self, amount):
        """
        Delete all cars up to the specified amount.

        :param amount: The number of cars to delete.
        """
        while amount > 0:
            self.web_driver.find_elements(MainPageLocators.EDIT_CAT_BTN.by,
                                          MainPageLocators.EDIT_CAT_BTN.locator)[0].click()
            self.__wait.until(
                EC.element_to_be_clickable(
                    (MainPageLocators.DELETE_CAR_BTN.by,
                     MainPageLocators.DELETE_CAR_BTN.locator))).click()
            self.__wait.until(
                EC.element_to_be_clickable(
                    (MainPageLocators.CONFIRM_DELETE_CAR_BTN.by,
                     MainPageLocators.CONFIRM_DELETE_CAR_BTN.locator))).click()

            amount -= 1
            time.sleep(3)

    def quit_driver(self):
        """
        Quit the WebDriver session to prevent resource leaks.
        """
        self.__web_driver.quit()
