from selenium.webdriver import Remote
from lesson_27.pages.base_page import BasePage
from lesson_27.locators.catalogue_item import CatalogueItemLocator as CIL


class MainPage(BasePage):

    def find_item_by_name(self, name):
        return self.web_driver.find_element(
            CIL.ITEM_NAME_LOCATOR.by, CIL.ITEM_NAME_LOCATOR.locator.format(name))
