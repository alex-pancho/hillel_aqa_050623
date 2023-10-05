import pytest

from lesson_27.locators.qauto_page_locators import MainPageLocators
from lesson_27.pages.qauto_page import BasePage

USERNAME = 'guest'
PASSWORD = 'welcome2qauto'
URL = 'qauto.forstudy.space'
USER_DATA = ('postolova.ira@gmail.com', '0aeJ7A8rdjUDaxk')


@pytest.fixture(scope='session')
def open_students_site():
    """
        Fixture for opening the QAuto student site with a guest user.

        This fixture opens the QAuto student site using the provided guest credentials.
        It yields the WebDriver instance and BasePage object for testing purposes.

        Yields:
            tuple: A tuple containing WebDriver instance and BasePage object.

        Usage:
            Use this fixture in your test functions to access the site with guest credentials.
        """
    page = BasePage()
    driver = page.web_driver
    try:
        driver.get(f'https://{USERNAME}:{PASSWORD}@{URL}')
        yield driver, page
    finally:
        driver.quit()


@pytest.fixture(scope='session')
def open_as_logged_user():
    """
        Fixture for opening the QAuto student site as a logged-in user.

        This fixture opens the QAuto student site, clicks the sign-in button,
        and logs in using the provided user data. It yields the WebDriver instance
        and BasePage object for testing purposes.

        Yields:
            tuple: A tuple containing WebDriver instance and BasePage object.

        Usage:
            Use this fixture in your test functions to access the site as a logged-in user.
        """
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
