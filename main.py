import threading

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from audio import player
from from_tests_locators import FromPageLocators
from window import show_message

URL = "https://proxy6.net/"
EMAIL = 'demo-tt1@inet-yar.ru'
PASSWORD = 'rNCV14la'

service = Service(ChromeDriverManager().install())
DRIVER = webdriver.Chrome(service=service)


class Login(FromPageLocators):
    def __init__(self, url, email, password):
        self.url = url
        self.email = email
        self.password = password

    def login_to_website(self, driver):

        driver.get(self.url)
        WebDriverWait(driver, timeout=5).until(
            EC.presence_of_element_located(FromPageLocators.BTN_PRIMARY)).click()
        WebDriverWait(driver, timeout=5).until(
            EC.presence_of_element_located(FromPageLocators.EMAIL)).send_keys(self.email)
        WebDriverWait(driver, timeout=5).until(
            EC.presence_of_element_located(FromPageLocators.PASSWORD)).send_keys(self.password)
        window = show_message()
        if window is True:
            WebDriverWait(driver, timeout=5).until(
                EC.presence_of_element_located(FromPageLocators.BTN_APPLY)).click()

            elements_ip = WebDriverWait(driver, timeout=10).until(
                EC.visibility_of_all_elements_located(FromPageLocators.IP_PORT))
            elements_time = WebDriverWait(driver, timeout=10).until(
                EC.visibility_of_all_elements_located(FromPageLocators.TIME_IP_PORT))
            texts_ip = [element.text for element in elements_ip]
            texts_time = [element.text for element in elements_time]

            for ip, time in zip(texts_ip, texts_time):
                print(f"{ip} - {time}")

            driver.quit()
        else:
            driver.quit()


def main():
    music_thread = threading.Thread(target=player.play)
    music_thread.start()

    new = Login(URL, EMAIL, PASSWORD)
    new.login_to_website(DRIVER)
    music_thread.join()


if __name__ == '__main__':
    main()
