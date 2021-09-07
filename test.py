import pytest
import selenium
from page_objects.LoginAdminPage import LoginAdminPage
from conftest import get_page


@pytest.mark.parametrize('page_name',
                         ['admin_page',
                          'home_page'])
def test_important_elements(browser, url, page_name):
    # browser.implicitly_wait(5)
    page = get_page(page_name)
    browser.get(url + page.POSTFIX_URL)
    for element in page.ELEMENTS.values():
        browser.find_element(*element)

 '''
 todo:
    add wait function
    add custom name for results (optional)
 '''
def test_start_browser2(browser, url):
    assert browser.title == "Your Store"
