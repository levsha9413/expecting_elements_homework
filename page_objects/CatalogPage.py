from selenium.webdriver.common.by import By


class CatalogPage:
    POSTFIX_URL = '/index.php?route=product/category&path=20'
    ELEMENTS = {'desktops': (By.XPATH, '''//*[text()='Desktops (13)']'''),
                'apple_cinema': (By.XPATH, '''//a[text()='Apple Cinema 30"']'''),
                'canon': (By.XPATH, '''//a[text()='Canon EOS 5D']'''),
                'hp': (By.XPATH, '''//a[text()='HP LP3065']'''),
                'htc': (By.XPATH, '''//a[text()='HTC Touch HD']'''),
                'iphone': (By.XPATH, '''//a[text()='iPhone']'''),
                'ipod': (By.XPATH, '''//a[text()='iPod Classic']'''),
                'macbook': (By.XPATH, '''//a[text()='MacBook']'''),
                'macbook_air': (By.XPATH, '''//a[text()='MacBook Air']'''),
                'palm_treo_pro': (By.XPATH, '''//a[text()='Palm Treo Pro']'''),
                'test_product': (By.XPATH, '''//a[text()='Product 8']'''),
                'samsung': (By.XPATH, '''//a[text()='Samsung SyncMaster 941BW']'''),
                'sony_vaio': (By.XPATH, '''//a[text()='Sony VAIO']'''),
                'laptops': (By.XPATH, '''//*[text()='Laptops & Notebooks (5)']'''),
                'components': (By.XPATH, '''//*[text()='Components (2)']'''),
                'tablets': (By.XPATH, '''//*[text()='Tablets (1)']'''),
                'software': (By.XPATH, '''//*[text()='Software (0)']'''),
                'phones': (By.XPATH, '''//*[text()='Phones & PDAs (3)']'''),
                'cameras': (By.XPATH, '''//*[text()='Cameras (2)']'''),
                'mp3': (By.XPATH, '''//*[text()='MP3 Players (4)']''')
                }
