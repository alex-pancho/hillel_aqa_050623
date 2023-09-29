from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_site(url: str) -> webdriver:
    driver = webdriver.Firefox()
    driver.get(url)
    return driver


def find_element(driver, by, locator: str):
    try:
        element = driver.find_element(by, locator)
    except NoSuchElementException:
        print("element not found")
        return
    return element

def find_field(driver):
    return find_element(driver, By.XPATH, '//input[@placeholder="Номер посилки"]')

def find_button_search(driver):
    return find_element(driver, By.XPATH, '//input[@id="np-number-input-desktop-btn-search-en"]')


def search_input(element, text: str):
    element.clear()
    element.send_keys(text)
    element.send_keys(Keys.RETURN)

def click(element):
    element.click()

def check_result(driver):
    return find_element(driver, By.XPATH, '//div[@class="header__status-text"]')

def close_window(driver):
    return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="button v-btn v-btn--depressed v-btn--flat v-btn--outlined theme--light v-size--default"]')))

def status_2(driver):
    return find_element(driver,By.XPATH,'//div[@class="header__status-text"]')

def get_text(element):
        return element.text
