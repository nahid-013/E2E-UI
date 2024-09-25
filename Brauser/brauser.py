from selenium import webdriver
from .brauser_options  import set_options


URL = 'https://www.saucedemo.com/'
driver = webdriver.Chrome(options=set_options())

driver.maximize_window()
driver.get(url=URL)