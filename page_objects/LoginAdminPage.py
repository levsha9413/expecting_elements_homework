from selenium.webdriver.common.by import By


class LoginAdminPage:
    POSTFIX_URL = '/admin'
    ELEMENTS = {'username_input': (By.ID, "input-username"),
                'password_input': (By.NAME, "password")}




''' SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
 OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
 FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
'''
