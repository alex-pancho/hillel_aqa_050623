import pytest

from hillel_aqa_050623.lesson_27.locators.locators_qauto_page import MainPageLocators
from hillel_aqa_050623.lesson_27.pages.qauto_page import BasePage

USERNAME = 'guest'
PASSWORD = 'welcome2qauto'
URL = 'qauto.forstudy.space'
USER_DATA = ('userok@mailforspam.com', 'q1q1q1q1A')


@pytest.fixture(scope='session')
def open_students_site():
    page = BasePage()
    driver = page.web_driver
    try:
        driver.get(f'https://{USERNAME}:{PASSWORD}@{URL}')
        yield driver, page
    finally:
        driver.quit()


@pytest.fixture(scope='session')
def open_as_logged_user():
    page = BasePage()
    driver = page.web_driver
    try:
        driver.get(f'https://{USERNAME}:{PASSWORD}@{URL}')
        # CLICK SIGN IN LOGIN
        driver.find_element(MainPageLocators.SIGN_IN_BTN.by, MainPageLocators.SIGN_IN_BTN.locator).click()
        # FILL SIGN IN FORM
        page.login_as_user(*USER_DATA)

        yield driver, page
    finally:
        driver.quit()
