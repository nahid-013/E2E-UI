from selenium import webdriver
from fake_useragent import UserAgent
def set_options():
    ua = UserAgent()
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={ua.random}')

    # disable webdriver mode
    options.add_argument("--disable-blink-features=AutomationControlled")

    # disable  mode
    # options.add_argument('--headless')
    return options