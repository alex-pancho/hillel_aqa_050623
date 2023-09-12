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
from main_hw25 import get_site, find_field, search_input, click
from main_hw25 import close_window, status_2, get_text

def test_menu():
    url = "https://tracking.novaposhta.ua/#/uk/"
    driver = get_site(url)
    element = find_field(driver)
    search_input(element, "59000965885218")
    button_2 = close_window(driver)
    click(button_2)
    element=status_2(driver)
    text=get_text(element)
    assert text=='Посилка отримана','Посилка не найдена'
    driver.close()
