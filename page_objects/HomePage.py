from selenium.webdriver.common.by import By


class HomePage:
    POSTFIX_URL = ''
    ELEMENTS = {'home_link': (By.XPATH, '''//a[contains(@href, "/index.php?route=common/home")]''')}
               # 'password_input': (By.NAME, "password")}