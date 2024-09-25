from logging import getLogger
import time

loger = getLogger(__name__)
def chek_purchase(By, driver):
    chek_result = driver.find_element(by=By.XPATH, value='//span[@data-test="title"]')
    loger.info('Покупка пользователя подтверждена')
    time.sleep(2)