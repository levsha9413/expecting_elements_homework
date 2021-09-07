import pytest
from selenium import webdriver
import os
from page_objects.LoginAdminPage import LoginAdminPage
from page_objects.HomePage import HomePage

DRIVERS = os.path.expanduser("~/qa/drivers")


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")  # headless режим нужен для разработчика
    parser.addoption("--browser", default="chrome", choices=["chrome", "firefox", "opera"])
    parser.addoption("--url", default="https://demo.opencart.com/")


@pytest.fixture  # делаем для url отдельную фикстуру, чтобы передавать как отдельный аргумент
def url(request):
    url = request.config.getoption("--url")
    return url


@pytest.fixture(scope="session")
def browser(request):
    _browser = request.config.getoption("--browser")  # _ добавляем для отличия от имени фикстуры
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    if _browser == "chrome":
        driver = webdriver.Chrome(
            executable_path=f"{DRIVERS}/chromedriver")  # создаем экземпляр драйвера, для этого нужно либо указать путь до драйвера, либо добавить в PATH
    elif _browser == "opera":
        driver = webdriver.Opera(executable_path=f"{DRIVERS}/operadriver")
    elif _browser == "firefox":
        driver = webdriver.Firefox(
            executable_path=f"{DRIVERS}/geckodriver")  # без ecutebel_path= chrome запускается, но firefox и opera - нет

    def final():  # добавляем финалайзер, чтобы браузер закрывался после теста (chrome сам закрывается, отсальные - нет)
        driver.quit()

    request.addfinalizer(final)

    return driver  # return ставим после финалайзера, иначе финалайзер не выполнится


def get_page(page_name):
    page = None
    if page_name == 'admin_page':
        page = LoginAdminPage
    elif page_name == 'home_page':
        page = HomePage
    else:
        pass
    return page
