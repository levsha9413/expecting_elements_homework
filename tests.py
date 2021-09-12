import pytest
from conftest import get_page, find_element_with_wait


@pytest.mark.parametrize('page_name',
                         ['admin_page',
                          'home_page',
                          'product_page',
                          'catalog_page'])
def test_important_elements(browser, url, page_name):
    page = get_page(page_name)
    browser.get(url + page.POSTFIX_URL)
    for element in page.ELEMENTS.values():
        find_element_with_wait(*element, browser)
