from selenium.webdriver.common.by import By

from hillel_aqa_050623.lesson_27.locators.base_locators import BaseLocators


#from locators.base_locators import BaseLocators

class BasePageLocators(BaseLocators):
    GENERAL_MENU_TOPIC = (By.XPATH, '//a[@href="/ua/category/{}"]')
    