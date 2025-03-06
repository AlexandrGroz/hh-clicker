import time
from configs.config import config


def scroll_to_bottom():
    is_end = False
    height = config.driver.execute_script("return document.body.scrollHeight")

    while not is_end:
        config.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)
        height_new = config.driver.execute_script("return document.body.scrollHeight")
        if height == height_new:
            is_end = True
        else:
            height = height_new
