from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.utils import wait_until_page_loaded

USER_EMAIL = ''
USER_PASSWORD = ''


def login():
    driver.find_element_by_id("#email").send_keys(USER_EMAIL)
    driver.find_element_by_id("#pass").send_keys(USER_PASSWORD).send_keys(Keys.ENTER)
    wait_until_page_loaded(wait)


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument("incognito")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get('https://www.facebook.com/')
    wait = WebDriverWait(driver, 10)
    wait_until_page_loaded(wait)
    login()
