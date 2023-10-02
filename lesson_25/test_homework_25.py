from lesson_25 import get_site, get_text, close_window, parcel_status
from lesson_25 import find_search_tracker, click, \
    find_search_button, search_ttn

"""
Написати тест, що вводить трекінг посилки на сайті НП
https://tracking.novaposhta.ua/#/uk/
та отримує статус посилки  в теркінгу, напр.
"""


def test_received():
    """Case for received parcel."""
    url = 'https://tracking.novaposhta.ua/#/uk/'
    driver = get_site(url)
    search_field = find_search_tracker(driver)
    click(search_field)
    ttn = '20450479119519'
    search_ttn(search_field, ttn)
    search_button = find_search_button(driver)
    click(search_button)
    anons_window_close_button = close_window(driver)
    click(anons_window_close_button)
    element = parcel_status(driver)
    text = get_text(element)
    assert text == 'Отримана', 'element NOT found'
    driver.close()
