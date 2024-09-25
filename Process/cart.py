import random
from logging import getLogger
import time

loger = getLogger(__name__)

def add_to_cart(By, driver):
    items = driver.find_elements(by=By.XPATH, value='//div[@data-test="inventory-item"]')
    item = random.choice(items)
    item_name = item.find_element(by=By.XPATH, value='//div[@data-test="inventory-item-name"]').text
    item_to_card = item.find_element(by=By.CLASS_NAME, value="btn_inventory").click()
    cart = driver.find_element(by=By.CLASS_NAME, value='shopping_cart_link').click()
    loger.info('Товар %s добавлен в корзину', item_name)
    time.sleep(2)