from selenium.webdriver.common.by import By
from configs.config import config


def check_auth():
    config.driver.get(config.login_url)

    login_button = config.driver.find_elements(By.XPATH, '//button[@data-qa="account-signup-submit"]')
    if login_button:
        return False
    else:
        return True
