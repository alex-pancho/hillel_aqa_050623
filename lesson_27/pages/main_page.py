from selenium.webdriver import Remote

from hillel_aqa_050623.lesson_27.pages.base_page import BasePage
from hillel_aqa_050623.lesson_27.locators.catalogue_item import CatalogueItemLocator as CIL


# from pages.base_page import BasePage
# from locators.catalogue_item import CatalogueItemLocator as CIL


class MainPage(BasePage):

    # def __init__(self, web_driver):
    #     super().__init__(web_driver)
    #     self.web_driver.get("https://parfums.ua/ua/")


    def find_item_by_name(self, name):
        return self.web_driver.find_element(
            CIL.ITEM_NAME_LOCATOR.by, CIL.ITEM_NAME_LOCATOR.locator.format(name))
