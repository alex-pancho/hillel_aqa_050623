# Homework for lesson 25
"""
Написати тест, що вводить трекінг посилки на сайті НП
https://tracking.novaposhta.ua/#/uk/
та отримує статус посилки  в теркінгу, напр.
<div data-v-631babf2="" class="header__parcel-dynamic-status px-4 d-flex align-center">
<div data-v-631babf2="" class="d-flex flex-column status-icon mr-4 status-icon-grey">
<!----></div>
<div data-v-631babf2="" class="flex-grow-1"
<div data-v-631babf2="" class="header__status-header"> Зараз: </div><!---->
<div data-v-631babf2="" class="header__status-text"> Посилка отримана </div>
</div></div>
== Посилка отримана
"""

import pytest
from lesson_25 import get_site
from lesson_25 import NovaPoshtaLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Test data
TRACKING_NUMBER = "59001015044713"  # Replace with an actual tracking number


@pytest.fixture(scope="module")
def driver():
    driver = get_site("https://tracking.novaposhta.ua/#/uk/")
    yield driver
    driver.quit()


def test_valid_tracking(driver):
    wait = WebDriverWait(driver, 20)
    tracking_input = wait.until(EC.presence_of_element_located(NovaPoshtaLocators.TRACKING_INPUT))
    tracking_input.send_keys(TRACKING_NUMBER)

    track_button = wait.until(EC.element_to_be_clickable(NovaPoshtaLocators.TRACKING_BUTTON))
    track_button.click()

    status_text = wait.until(EC.presence_of_element_located(NovaPoshtaLocators.STATUS_TEXT))
    assert "Отримана" in status_text.text
