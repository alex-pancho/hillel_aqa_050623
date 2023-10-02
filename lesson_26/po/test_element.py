from elements import get_site, find_element, search_input, get_text
from locators import MainPageLocators as MPL


def test_search():
    url = "https://www.python.org"
    driver = get_site(url)
    find_field = find_element(driver, *MPL.find_field)
    assert find_field is not None
    search_input(find_field, "python")
    not_found = find_element(driver, *MPL.result_search_not_found)
    text = get_text(not_found)
    assert text != "No results found.", "Search doesn't work"


def test_search_second():
    url = "https://www.python.org"
    driver = get_site(url)
    find_field = find_element(driver, *MPL.find_field)
    assert find_field is not None
    search_input(find_field, "sdkjfhvjkvlhyl4uvuybjkefadsy89h")
    not_found = find_element(driver, *MPL.result_search_not_found)
    text = get_text(not_found)
    assert text == "No results found.", "Search doesn't work"
