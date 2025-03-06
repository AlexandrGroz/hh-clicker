from drivers.use_chrome_driver import use_chrome_driver


def set_driver(driver_type="chrome"):
    driver = None

    if driver_type.lower() == "chrome":
        driver = use_chrome_driver()

    return driver
