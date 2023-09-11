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

import time
from lesson_25 import get_site, find_element, find_field, click, not_found, search_input, get_text, search_field, status_message

def test_search_parsel():
    url = "https://tracking.novaposhta.ua"
    driver = get_site(url)
    element = search_field(driver)
    search_input(element, '20450771312334')
    time.sleep(5)
    element = status_message(driver)
    text = get_text(element)
    # print(text)
    assert text == 'Посилка отримана', f"text is wrong -{text}"
    driver.quit()

#  _____check_line_____


