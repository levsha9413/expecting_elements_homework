from selenium.webdriver.common.by import By


class HomePage:
    POSTFIX_URL = ''
    ELEMENTS = {'home_link': (By.XPATH, '''//a[contains(@href, "/index.php?route=common/home")]'''),
                'big_swiper': (By.XPATH, '''//div[@id='slideshow0']'''),
                'menu_bar': (By.XPATH, '''//nav[@id="menu"]'''),
                'product_bar': (By.XPATH, '''//div[@id="content"]/div[@class="row"]'''),
                'partners_swiper': (By.XPATH, '''//div[@id="carousel0"]'''),
                'footer': (By.XPATH, '''//footer'''),
                'search_panel': (By.XPATH, '''//input[@name = "search"]'''),
                'button_cart': (By.XPATH, '''//div[@id="cart"]/button''')
                }
