r"""HomeTask_25.

Написати тест, що вводить трекінг посилки на сайті НП
https://tracking.novaposhta.ua/#/uk/
та отримує статус посилки  в теркінгу, напр.
<div data-v-631babf2=
"" class="header__parcel-dynamic-status px-4 d-flex align-center">
<div data-v-631babf2=
"" class="d-flex flex-column status-icon mr-4 status-icon-grey">
<!----></div>
<div data-v-631babf2=
"" class="flex-grow-1"
<div data-v-631babf2=
"" class="header__status-header"> Зараз: </div><!---->
<div data-v-631babf2=
"" class="header__status-text"> Посилка отримана </div>
</div></div>
== Посилка отримана
"""

from lesson_25 import get_site, get_search_input
from lesson_25 import get_search_button, insert_text
from lesson_25 import click, get_accepting_element, get_status_text
from time import sleep


def test_track_number():
    """test_track_number function."""
    tracking_number = '59000995637241'
    url = 'https://tracking.novaposhta.ua/#/uk/'
    driver = get_site(url)
    el_btn = get_search_button(driver)
    el_input = get_search_input(driver)
    insert_text(el_input, tracking_number)
    click(el_btn)
    sleep(5)
    ac_btn = get_accepting_element(driver)
    click(ac_btn)
    sleep(5)
    status_text = get_status_text(driver).text
    print('Статус посилки:', status_text)
