from Brauser.brauser import driver

from selenium.webdriver.common.by import By

from Process.register import register_user
from Process.cart import add_to_cart
from Process.buy import buy_item
from Process.chek import chek_purchase

from logger import logger

def main():
    try:
        logger.info('Браузер запущен')
        register_user(By=By, driver=driver)
        add_to_cart(By=By, driver=driver)
        buy_item(By=By, driver=driver)
        chek_purchase(By=By, driver=driver)
    except Exception as e:
        print('Exception:', e)
    finally:
        driver.close()
        driver.quit()

if __name__ == '__main__':
    logger.info('ожидание...')
    main()