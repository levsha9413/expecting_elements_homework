from selenium.webdriver.common.by import By


class LoginAdminPage:
    POSTFIX_URL = '/admin'
    ELEMENTS = {'username_input': (By.ID, "input-username"),
                'password_input': (By.NAME, "password"),
                'logo': (By.XPATH, '''//img[@alt="OpenCart"]'''),
                'login_button': (By.XPATH, '''//button[text()=" Login"]'''),
                'panel_title': (By.XPATH, '''//h1[text()=" Please enter your login details."]'''),
                'forgotten_password_link': (By.XPATH,
                                            '''//a[text()="Forgotten Password" and\
                                              contains (@href, "admin/index.php?route=common/forgotten")]''')}
