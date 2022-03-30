from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from billing.methods.whatsappMethods import WhatsappMethods
from telegram_pack.send_telegram import send_to_telegram
from billing.locators.greenApiLocators import GreenApiLocators
from telegram_pack.config import TOKEN

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/home/butovich_v/workspace/whatsapp/driver/chromedriver_lnx')

wa = WhatsappMethods(driver)

gal = GreenApiLocators

wa.go_to_green_api_page()

time.sleep(5)

wa.authorize_green_api()

time.sleep(5)

wa.go_to_first_project_url()

time.sleep(5)

first_account_status = wa.chek_status()

if first_account_status == 'Не авторизован':
    message = 'Статус аккаунта [21269](https://cabinet.green-api.com/waInstance/21269): Не авторизован.'
    print(message)
    send_to_telegram(message, TOKEN, '-1001179024349')

elif first_account_status == 'Не оплачен':
    message = 'Статус аккаунта [21269](https://cabinet.green-api.com/waInstance/21269): Не оплачен.'
    print(message)
    send_to_telegram(message, TOKEN, '-1001179024349')

wa.go_to_second_project_url()

time.sleep(5)

second_account_status = wa.chek_status()

if second_account_status == 'Не авторизован':
    message = 'Статус аккаунта [26564](https://cabinet.green-api.com/waInstance/26564): Не авторизован.'
    print(message)
    send_to_telegram(message, TOKEN, '-1001179024349')

elif second_account_status == 'Не оплачен':
    message = 'Статус аккаунта [26564](https://cabinet.green-api.com/waInstance/26564): Не оплачен.'
    print(message)
    send_to_telegram(message, TOKEN, '-1001179024349')

driver.quit()
