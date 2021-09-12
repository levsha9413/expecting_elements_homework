import pytest
from selenium import webdriver
import os
from page_objects.LoginAdminPage import LoginAdminPage
from page_objects.HomePage import HomePage
from page_objects.ProductPage import ProductPage
from page_objects.CatalogPage import CatalogPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

DRIVERS = os.path.expanduser("~/qa/drivers")


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")  # headless режим нужен для разработчика
    parser.addoption("--browser", default="chrome", choices=["chrome", "firefox", "opera"])
    parser.addoption("--url", default="https://demo.opencart.com/")


@pytest.fixture
def url(request):
    url = request.config.getoption("--url")
    return url


@pytest.fixture(scope="session")
def browser(request):
    _browser = request.config.getoption("--browser")

    if _browser == "chrome":
        driver = webdriver.Chrome(
            executable_path=f"{DRIVERS}/chromedriver")
    elif _browser == "opera":
        driver = webdriver.Opera(executable_path=f"{DRIVERS}/operadriver")
    elif _browser == "firefox":
        driver = webdriver.Firefox(
            executable_path=f"{DRIVERS}/geckodriver")

    def final():
        driver.quit()

    request.addfinalizer(final)

    return driver


def get_page(page_name):  # функция для передачи одной из страниц по полученному параметру
    page = None
    if page_name == 'admin_page':
        page = LoginAdminPage
    elif page_name == 'home_page':
        page = HomePage
    elif page_name == 'product_page':
        page = ProductPage
    elif page_name == 'catalog_page':
        page = CatalogPage
    else:
        pass
    return page


def find_element_with_wait(locator, selector, driver, timeout=5):
    # кастомный поиск элемента с ожидаением по существованию элемента
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((locator, selector)))
    except TimeoutException:
        raise AssertionError("Не найден элемент с селектором: {}".format(selector))
