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
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

URL = 'https://tracking.novaposhta.ua/#/uk/'
PARCEL_CODE = '20450762667993'


@pytest.mark.parametrize('parcel_code',
                         [pytest.param(PARCEL_CODE, id=f'test_tracking_novaposhta with parcel_code {PARCEL_CODE}')])
def test_tracking_novaposhta(parcel_code):
    # Create driver
    driver = webdriver.Chrome()

    # Go to URL
    driver.get(URL)