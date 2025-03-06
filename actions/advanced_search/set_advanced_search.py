import time
from configs.config import config
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def clear_region():
    while True:
        try:
            regions = config.driver.find_elements(By.XPATH, '//div[@data-qa="chip"]')

            if not regions:
                break

            for region in regions:
                try:
                    delete_button = region.find_element(By.XPATH, './/button[@data-qa="chip-delete-action"]')
                    config.wait.until(EC.element_to_be_clickable(delete_button))
                    config.driver.execute_script("arguments[0].click();", delete_button)

                except Exception as e:
                    print(f"Ошибка при удалении элемента: {e}")
                    continue

        except Exception as e:
            print(f"Ошибка при получении списка регионов: {e}")
            break


def set_region():
    set_region_button = config.driver.find_element(By.XPATH, '//button[@data-qa="advanced-search-region-selectFromList"]')
    config.driver.execute_script("arguments[0].click();", set_region_button)

    region_input = config.wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-qa="tree-selector-search-input"]')))
    region_input.send_keys(config.region.lower())
    time.sleep(2)

    try:
        region_block = config.driver.find_element(
            By.XPATH,
            f'''//div[contains(@data-qa, "tree-selector-item") and 
                .//div[contains(
                    translate(normalize-space(.), 
                        "ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ", 
                        "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
                    ), "{config.region.lower()}"
                )]
            ]'''
        )
        config.action.click(region_block).perform()
        config.action.click(config.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-qa = "composite-selection-tree-selector-modal-submit"]')))).perform()

    except Exception as e:
        print(f"Ошибка при получении города: {e}")


def set_advanced_search():
    config.driver.get(config.base_page)

    config.action.click(config.wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@data-qa="advanced-search"]')))).perform()

    clear_region()

    if config.region.lower() != "global":
        set_region()

    advanced_search_input= config.wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-qa="vacancysearch__keywords-input"]')))
    config.driver.execute_script('arguments[0].value = arguments[1]', advanced_search_input, config.search_query)

    exclude_input = config.wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-qa="vacancysearch__keywords-excluded-input"]')))
    config.driver.execute_script('arguments[0].value = arguments[1]', exclude_input, config.search_exclude)

    delete_agency = config.driver.find_element(By.XPATH, '//input[@data-qa="advanced-search__label-item_not_from_agency"]')
    config.driver.execute_script('arguments[0].click()', delete_agency)

    items_on_page = config.driver.find_element(By.XPATH, '//input[@data-qa="advanced-search__items_on_page-item_100"]')
    config.driver.execute_script("arguments[0].click()", items_on_page)

    advanced_search_apply_button = config.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-qa="advanced-search-submit-button"]')))
    config.driver.execute_script("arguments[0].click()", advanced_search_apply_button)

