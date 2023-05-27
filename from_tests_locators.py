from selenium.webdriver.common.by import By


class FromPageLocators:

    BTN_PRIMARY = (By.CSS_SELECTOR, "a[class='btn']")
    EMAIL = (By.CSS_SELECTOR, "div.input-group input[name='email']")
    PASSWORD = (By.CSS_SELECTOR, "div.input-group input[name='password']")
    BTN_APPLY = (By.CSS_SELECTOR, "div.form button[type= 'submit']")
    IP_PORT = (By.CSS_SELECTOR, "div[class='right clickselect ']")
    TIME_IP_PORT = (By.CSS_SELECTOR, "div[class='right color-success']")


