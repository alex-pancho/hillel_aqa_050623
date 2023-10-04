from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


def get_site(url: str) -> webdriver:
    driver = webdriver.Chrome()
    driver.get(url)
    return driver


def find_element(driver, by, locator: str):
    try:
        element = driver.find_element(by, locator)
    except NoSuchElementException:
        print("element not found")
        return
    return element


def get_search_input(driver):
    return find_element(driver, By.ID, "en")

def get_search_button(driver):
    return find_element(driver, By.ID, "np-number-input-desktop-btn-search-en")

def insert_text(element, str):
    element.send_keys(str)


def click(element):
    element.click()

def get_accepting_element(driver):
    return find_element(driver, By.CSS_SELECTOR, '.first-visit-helper-wrapper .button')


def search_input(element, text: str):
    element.clear()
    element.send_keys(text)
    element.send_keys(Keys.RETURN)


def get_status_text(driver):
    return find_element(driver, By.XPATH, '//*[@id="chat"]/header/div[2]/div[2]/div[2]')
