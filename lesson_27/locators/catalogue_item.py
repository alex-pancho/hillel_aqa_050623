from selenium.webdriver.common.by import By
from lesson_27.locators.base_locators import BaseLocators


class CatalogueItemLocator(BaseLocators):
    PRICE_LOCATOR = (By.XPATH, '//span[@class="price_item"]')
    ITEM_NAME_LOCATOR = (By.XPATH, '//a[@data-default-name="{}"]')