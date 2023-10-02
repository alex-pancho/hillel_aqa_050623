from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_site(url: str) -> webdriver:
    driver = webdriver.Firefox()
    # driver = webdriver.Chrome()
    driver.get(url)
    return driver


def find_element(driver, by, locator: str):
    try:
        # element = driver.find_element(by, locator)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((by, locator))
        )
    except NoSuchElementException:
        print("element not found")
        return
    return element


def find_field(driver):
    return find_element(driver, By.XPATH, '//input[@type="search"]')


def not_found(driver):
    return find_element(driver, By.XPATH,
                        '//ul[@class="list-recent-events menu"]/p')


def search_input(element, text: str):
    element.clear()
    element.send_keys(text)
    element.send_keys(Keys.RETURN)


def get_text(element):
    return element.text


def test_search():
    url = "https://www.python.org"
    driver = get_site(url)
    element = find_field(driver)
    search_input(element, "python")
    element = not_found(driver)
    text = get_text(element)
    assert text != "No results found.", "Search doesn't work"
