from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from configs.config import config


def use_phone():
    config.driver.get(config.login_url)
    login_input = config.wait.until(EC.element_to_be_clickable((By.NAME, 'login')))
    login_input.clear()
    login_input.send_keys(config.phone)

    send_code_button = config.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-qa="account-signup-submit"]')))
    config.action.click(send_code_button).perform()
    code_from_sms = input("Введите код из СМС и нажми Enter: ")

    config.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-qa='otp-code-input']"))).send_keys(code_from_sms)

    enter_button = config.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='otp-code-submit']")))
    config.action.click(enter_button).perform()