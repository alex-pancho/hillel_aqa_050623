from selenium.webdriver.common.by import By
from locators.base_locators import BaseLocators

class BasePageLocators(BaseLocators):
    GENERAL_MENU_TOPIC = (By.XPATH, '//a[@href="/ua/category/{}"]')
    