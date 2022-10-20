import datetime
import time

from django.core.management import BaseCommand
import telebot
from selenium import webdriver

from apps.items import utils
from apps.items.utils import token

options = webdriver.ChromeOptions()
options.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
)
options.add_extension('/home/yaroslav/projects/steam_bot/steam_bot/easy_money/chromedriver/helper.crx')
driver = webdriver.Chrome(
    executable_path="/home/yaroslav/projects/steam_bot/steam_bot/easy_money/chromedriver/chromedriver",
    options=options
)


class Command(BaseCommand):
    def handle(self, *args, **options):
        bot = telebot.TeleBot(token)
        driver.get(utils.login_url)
        time.sleep(20)

        @bot.message_handler(commands=['start'])
        def send_text_name_tag(message):
            balance = 0
            while True:
                driver.get('https://steamcommunity.com/profiles/76561198273688543')
                print(balance)
                try:
                    get_balance = float(driver.find_elements_by_id('header_wallet_balance')[0].text[1:6])
                    if get_balance > balance:
                        profit = get_balance - balance
                        balance = get_balance
                        bot.send_message(message.chat.id, f"Your balance has increased by: {profit}")

                    elif get_balance < balance:
                        price = balance-get_balance
                        balance = get_balance
                        bot.send_message(message.chat.id, f'You bought something for: ${price}')

                        # driver.find_element_by_class_name('inventory_page').find_elements_by_class_name('itemHolder')[
                        #     0].click()
                        # print(f"0--{driver.find_elements_by_class_name('item_desc_description')[0].text[:4]}")
                        # print(f"1--{driver.find_elements_by_class_name('item_desc_description')[1].text[:4]}")
                        # if driver.find_elements_by_id('iteminfo0_item_name')[0].text[:4] != 'Ключ':
                        #     title = driver.find_elements_by_xpath('//*[@id="iteminfo0_item_name"]')[0].text
                        #     bot.send_message(message.chat.id,
                        #                      f"Buy new item: {title}"
                        #                      )
                    time.sleep(60)

                except Exception:
                    time_now = datetime.datetime.now()
                    print(f"Page refresh error: {time_now}")
                    time.sleep(60)

        bot.polling()
