import pytest
from selenium import webdriver
import os

DRIVERS = os.


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless") # headless режим нужен для разработчика
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox", "opera"])
    parser.addoption("--url", action="store", default="https://demo.opencart.com/")


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")  # _ добавляем для отличия от имени фикстуры
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    if _browser == "chrome":
        driver = webdriver.Chrome() # создаем экземпляр драйвера, для этого нужно либо указать путь до драйвера, либо добавить в PATH
    elif _browser == "opera":
        driver = webdriver.Opera()
    elif _browser == "firefox":
        driver = webdriver.Firefox()
