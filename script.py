import os
from actions.vacancies_actions.click_vacanies import click_vacancies
from actions.login.login import login
from actions.advanced_search.set_advanced_search import set_advanced_search
from configs.config import config
from helpers.check_bat import is_running_from_batch


def start_clicking():
    login()
    set_advanced_search()

    while config.counter < config.limit:
        click_vacancies()

    config.driver.close()
    config.driver.quit()


if __name__ == "__main__":
    start_clicking()
