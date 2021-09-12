from selenium.webdriver.common.by import By


class ProductPage:
    POSTFIX_URL = '/index.php?route=product/product&path=20&product_id=42'
    ELEMENTS = {'page_title': (By.XPATH, '''//head/title[text()='Apple Cinema 30']'''),
                'product_name': (By.XPATH, '''//h1[text()='Apple Cinema 30"']'''),
                'tab_description': (By.XPATH, '''//a[@href="#tab-description"]'''),
                'tab_specification': (By.XPATH, '''//a[@href="#tab-specification"]'''),
                'tab_review': (By.XPATH, '''//a[@href="#tab-review"]'''),
                'description_content': (By.XPATH, '''//div[@class='tab-content']'''),
                'current_price': (By.XPATH, '''//h2[text()='$110.00']''')}
