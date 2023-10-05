from selenium.webdriver import Remote, ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from lesson_27.locators.base_page import BasePageLocators
from lesson_27.locators.catalogue_item import CatalogueItemLocator


class BasePage:

    def __init__(self, web_driver):
        self.__web_driver = web_driver
        self.__action = ActionChains(self.__web_driver)
        self.__wait = WebDriverWait(self.__web_driver, 15)

    @property
    def web_driver(self):
        return self.__web_driver

    @property
    def action(self):
        return self.__action

    @property
    def wait(self):
        return self.__wait

    def get_menu_item(self, data_item):
        return self.__wait.until(
            expected_conditions.element_to_be_clickable(
                (BasePageLocators.GENERAL_MENU_TOPIC.by,
                 BasePageLocators.GENERAL_MENU_TOPIC.locator.format(data_item)
                )
            )
        )
    

    def go_to_women_parfumes(self):
        self.get_menu_item(
            CatalogueItemLocator.PRICE_LOCATOR.value
        )
