
from selenium import webdriver

from hillel_aqa_050623.lesson_27.pages.main_page import MainPage


def test_woman_parfume():
    main_page = MainPage(webdriver.Firefox())
    woman_parfumes_catalogue = main_page.go_to_women_parfumes()
    parfume_name = "Lanvin Eclat D\'Arpege"
    expected_price = "633"
    actual_price = woman_parfumes_catalogue.find_item_by_name(parfume_name).text

    assert expected_price == actual_price