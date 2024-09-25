from logging import getLogger
import time

loger = getLogger(__name__)

def buy_item(By, driver):
    buy = driver.find_element(by=By.ID, value='checkout').click()
    input_firsе_name = driver.find_element(by=By.ID, value="first-name")
    input_firsе_name.clear()
    input_firsе_name.send_keys('User')
    time.sleep(2)

    input_last_name = driver.find_element(by=By.ID, value="last-name")
    input_last_name.clear()
    input_last_name.send_keys('password')
    time.sleep(2)
    input_postal_code = driver.find_element(by=By.ID, value="postal-code")
    input_postal_code.clear()
    input_postal_code.send_keys('112233')
    time.sleep(2)
    continue_btn = driver.find_element(by=By.ID, value="continue").click()
    finish_btn = driver.find_element(by=By.ID, value="finish").click()
    loger.info('Товар куплен')