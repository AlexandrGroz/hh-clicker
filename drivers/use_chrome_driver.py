import chromedriver_autoinstaller
from selenium import webdriver


def use_chrome_driver():
    chromedriver_autoinstaller.install()
    options = webdriver.ChromeOptions()
    options.add_argument('--allow-profiles-outside-user-dir')
    options.add_argument('--enable-profile-shortcut-manager')
    options.add_argument(r'user-data-dir=C:\Users\se661\AppData\Local\Google\Chrome\User Data')
    options.add_argument('--profile-directory=Profile 1')
    driver = webdriver.Chrome(options=options)
    return driver
