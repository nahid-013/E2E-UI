from selenium.webdriver.common.keys import Keys
from logging import getLogger
import time

loger = getLogger(__name__)

def register_user(By, driver):
    input_username = driver.find_element(by=By.ID, value="user-name")
    input_username.clear()
    input_username.send_keys('standard_user')
    time.sleep(2)
    input_password = driver.find_element(by=By.ID, value="password")
    input_password.clear()
    input_password.send_keys('secret_sauce')
    time.sleep(2)
    input_password.send_keys(Keys.ENTER)
    loger.info('Пользователь успешно зарегестрирован')
    time.sleep(2)