from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


def get_site(url: str) -> webdriver:
    driver = webdriver.Chrome()
    driver.get(url)
    return driver


def get_hillel(user: str = "guest", passw: str = "welcome2qauto"):
    return get_site(f"https://{user}:{passw}@qauto.forstudy.space/")


def find_element(driver, by, locator: str):
    try:
        element = driver.find_element(by, locator)
    except NoSuchElementException:
        print("element not found")
        return
    return element


# Home_Page
def get_home_button(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[1]/nav/a')


def get_about_button(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[1]/nav/button[1]')


def get_contacts_button(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[1]/nav/button[2]')


# Log_in
def get_sign_in_button(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[2]/button[2]')


def get_email_input(driver):
    return find_element(driver, By.ID, 'signinEmail')


def get_password_input(driver):
    return find_element(driver, By.ID, 'signinPassword')


def get_login_button(driver):
    return find_element(driver, By.XPATH, '/html/body/ngb-modal-window/div/div/app-signin-modal/div[3]/button[2]')


# Panel_User_Menu

def get_panel_garage_button(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[1]/nav/a[1]')


def get_panel_full_expenses_button(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[1]/nav/a[2]')


def get_panel_instructions_button(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[1]/nav/a[2]')

def get_panel_profile_button(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[1]/nav/div/a[1]')


def get_panel_settings_button(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[1]/nav/div/a[2]')


def get_panel_logaut_button(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[1]/nav/a[4]')


# Header_User_Menu

def get_header_logo_button(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div/a/svg')


def get_header_garage_button(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div/nav/a[1]')


def get_header_full_expenses_button(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div/nav/a[2]')


def get_header_instructions_button(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div/nav/a[3]')


# Dropdown_User_Menu

def get_dropdown_my_profile_button(driver):
    return find_element(driver, By.ID, 'userNavDropdown')


def get_dropdown_garage_button(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/app-user-nav/div/nav/a[1]')


def get_dropdown_full_expenses_button(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/app-user-nav/div/nav')


def get_dropdown_instructions_button(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/app-user-nav/div/nav/a[3]')


def get_dropdown_profile_button(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/app-user-nav/div/nav/div[1]/a[1]')


def get_dropdown_settings_button(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/app-user-nav/div/nav/div[1]/a[2]')


def get_dropdown_logout_button(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/app-user-nav/div/nav/button')

# Garage


def get_add_car_button(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[1]/button')


def get_brand_car_button(driver):
    return find_element(driver, By.ID, 'addCarBrand')


def get_select_brand_car_button(driver,car):
    click(get_brand_car_button(driver))
    return find_element(driver, By.XPATH, '//select[@id = "addCarBrand"]/option[contains(text(),"' + car +'")]')


def get_model_car_button(driver):
    return find_element(driver, By.ID, 'addCarModel')


def get_select_model_car_button(driver,model):
    click(get_model_car_button(driver))
    return find_element(driver, By.XPATH, '//select[@id = "addCarModel"]/option[contains(text(),"' + model +'")]')


def get_mileage_button(driver):
    return find_element(driver, By.ID, 'addCarMileage')


def get_mileage_counter_button(driver):
    return find_element(driver, By.XPATH, '//*[@id="addCarMileage"]')


def get_add_button(driver):
    return find_element(driver, By.XPATH, '/html/body/ngb-modal-window/div/div/app-add-car-modal/div[3]/button[2]')


def get_cancel_button(driver):
    return find_element(driver, By.XPATH, '/html/body/ngb-modal-window/div/div/app-add-car-modal/div[3]/button[1]')


def get_mileage_update_button(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[2]/div/ul/li[1]/app-car/div/div[2]/app-update-mileage-form/form/button')


def get_mileage_update_value(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[2]/div/ul/li[1]/app-car/div/div[2]/app-update-mileage-form/form/input')


def get_edit_button(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[2]/div/ul/li[1]/app-car/div/div[1]/div[2]/button[1]/span')


def get_save_button(driver):
    return find_element(driver, By.XPATH, '/html/body/ngb-modal-window/div/div/app-edit-car-modal/div[3]/div/button[2]')


def get_add_expenseliters(driver):
    return find_element(driver, By.ID, 'addExpenseLiters')


def get_add_expensetotalcost(driver):
    return find_element(driver, By.ID, 'addExpenseTotalCost')


def get_add_fuel_expense(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[2]/div/ul/li[1]/app-car/div/div[1]/div[2]/button[2]')


def get_add_fuelexpense_button(driver):
    return find_element(driver, By.XPATH, '/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[3]/button[2]')


def get_remove_car(driver):
    return find_element(driver, By.XPATH, '/html/body/ngb-modal-window/div/div/app-edit-car-modal/div[3]/button')


def get_remove_button(driver):
    return find_element(driver, By.XPATH, '/html/body/ngb-modal-window/div/div/app-remove-car-modal/div[3]/button[2]')


def get_remove_fuel_expense(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-fuel-expenses/div/div[2]/div/div[1]/table/tbody/tr/td[5]/button[1]/span')


def get_select_fuel_expense(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-fuel-expenses/div/div[2]/div/div[1]/table/tbody/tr/td[5]')


def get_delete_fuel_expense(driver):
    click(get_select_fuel_expense(driver))
    return find_element(driver, By.XPATH, '//html/body/ngb-modal-window/div/div/app-delete-expense-modal/div[3]/button[2]')

# Contacts


def get_contacts_button(driver):
    return find_element(driver, By.XPATH, '/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[1]/nav/button[2]')


def get_facebook_button(driver):
    return find_element(driver, By.XPATH, '//*[@id="contactsSection"]/div/div/div[1]/div/a[1]/span')


def get_telegram_button(driver):
    return find_element(driver, By.XPATH, '//*[@id="contactsSection"]/div/div/div[1]/div/a[2]/span')


def get_youtube_button(driver):
    return find_element(driver, By.XPATH, '//*[@id="contactsSection"]/div/div/div[1]/div/a[3]/span')


def get_instagram_button(driver):
    return find_element(driver, By.XPATH, '//*[@id="contactsSection"]/div/div/div[1]/div/a[4]/span')


def get_linkedin_button(driver):
    return find_element(driver, By.XPATH, '//*[@id="contactsSection"]/div/div/div[1]/div/a[5]/span')


def get_hillel_website_button(driver):
    return find_element(driver, By.XPATH, '//*[@id="contactsSection"]/div/div/div[2]/a[1]')


def get_mail_button(driver):
    return find_element(driver, By.XPATH, '//*[@id="contactsSection"]/div/div/div[2]/a[2]')


def insert_text(element, str):
    element.send_keys(str)


def click(element):
    element.click()


def search_input(element, text: str):
    element.clear()
    element.send_keys(text)
    element.send_keys(Keys.RETURN)
