from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_site(url: str) -> webdriver:
    """Open browser with the given URL."""
    driver = webdriver.Firefox()
    driver.get(url)
    return driver


def find_element(driver, by, locator: str):
    """Error element not found."""
    try:
        element = driver.find_element(by, locator)
    except NoSuchElementException:
        print("Element does NOT found")
        return
    return element


def find_search_tracker(driver):
    """Find search field."""
    return find_element(driver, By.ID, 'en')


def find_search_button(driver):
    """Find search button."""
    return find_element(driver, By.ID, 'np-number-input-desktop-btn-search-en')


def click(element):
    """Click element."""
    element.click()


def search_ttn(element, text: str):
    """Input data."""
    element.clear()
    element.send_keys(text)


def get_text(element):
    """Get text."""
    return element.text


def close_window(driver):
    """
    Wait for and return a clickable element to close a window.
    """
    return WebDriverWait(driver, 10). \
        until(EC.element_to_be_clickable
              ((By.XPATH,
                '//button[@class="button v-btn v-btn--depressed '
                'v-btn--flat v-btn--outlined theme--light '
                'v-size--default"]')))


def parcel_status(driver):
    """
    Find and return the parcel status element on the page.
    """
    return find_element(driver, By.XPATH,
                        '//div[@class="header__status-text"]')
