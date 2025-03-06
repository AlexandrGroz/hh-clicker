from configs.config import config


def highlight_blocks(elements):
    if len(elements) > 1:
        for element in elements:
            config.driver.execute_script("arguments[0].style.border='3px solid red';", element)
    else:
        config.driver.execute_script("arguments[0].style.border='3px solid red';", elements[0])

