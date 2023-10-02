from selenium.webdriver.common.by import By


class MainPageLocators():

    find_field = (By.XPATH, '//input[@type="search"]')
    result_search_not_found = (By.XPATH,
                               '//ul[@class="list-recent-events menu"]/p')
