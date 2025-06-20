import chromedriver_autoinstaller
from selenium import webdriver


def use_chrome_driver():
    chromedriver_autoinstaller.install()
    options = webdriver.ChromeOptions()

    options.add_argument(r'--user-data-dir=C:\selenium_profile')
    options.add_argument('--profile-directory=Default')

    # Подавляем шумящие логи
    options.add_argument('--log-level=3')
    options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com")
    return driver