import time
from actions.vacancies_actions.find_vacancies import find_vacancies
from configs.config import config
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def click_vacancies():
    vacancies_list = find_vacancies()
    if len(vacancies_list) > 0:
        for vacancy in vacancies_list:
            if config.counter != config.limit:
                apply_button = vacancy.find_element(By.XPATH, './/a[@data-qa="vacancy-serp__vacancy_response"]')
                a = apply_button.get_attribute('href')
                config.driver.execute_script("window.open('');")
                config.driver.switch_to.window(config.driver.window_handles[1])
                config.driver.get(a)
                config.wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "main-content")]')))
                time.sleep(1)
                config.increment_counter()
                config.driver.close()
                config.driver.switch_to.window(config.driver.window_handles[0])
            else:
                break
    else:
        raise Exception("Подходящих вакансий не найдено.")
