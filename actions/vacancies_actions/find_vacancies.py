from configs.config import config
from selenium.webdriver.common.by import By
from helpers.highlights import highlight_blocks


def find_vacancies():
    vacancies = config.driver.find_elements(
        By.XPATH,
        '//div[contains(@data-qa, "vacancy-serp__vacancy") and '
        './/span[contains(text(), "Откликнуться")]]'
    )
    highlight_blocks(vacancies)
    return vacancies
