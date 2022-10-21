import datetime
import time

import telebot
from django.core.management.base import BaseCommand, CommandError
from selenium import webdriver

from apps.items import utils
from apps.items.models import Item
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
            while True:
                for item in Item.objects.filter(is_active=True):
                    try:
                        driver.get(item.link)
                        for ind, element in enumerate(
                                driver.find_element_by_id('searchResultsRows').find_elements_by_class_name(
                                    'market_listing_row')[:5]
                        ):
                            price = driver.find_elements_by_class_name('market_listing_their_price')[ind].text[1:5]
                            if element.find_elements_by_class_name('sih-fraud'):
                                driver.find_elements_by_class_name('market_listing_buy_button')[ind].click()
                                print('try buy')
                                driver.find_elements_by_xpath('//*[@id="market_buynow_dialog_accept_ssa"]')[0].click()
                                driver.find_elements_by_xpath('//*[@id="market_buynow_dialog_purchase"]')[0].click()
                                bot.send_message(
                                    message.chat.id,
                                    f"You bought {item.title} with a name tag for ${price}"
                                )

                        for ind, element in enumerate(driver.find_elements_by_xpath('//div[@class="sih-images"]')[:3]):
                            price = driver.find_elements_by_class_name('market_listing_their_price')[ind].text[1:5]
                            count_elements = len(element.find_elements_by_class_name('sticker-image'))
                            if count_elements == 4 and float(price) <= item.price_4 or \
                                    count_elements == 3 and float(price) <= item.price_3:
                                driver.find_elements_by_class_name('market_listing_buy_button')[ind].click()
                                print('try buy')
                                driver.find_elements_by_xpath('//*[@id="market_buynow_dialog_accept_ssa"]')[0].click()
                                driver.find_elements_by_xpath('//*[@id="market_buynow_dialog_purchase"]')[0].click()
                                bot.send_message(
                                    message.chat.id,
                                    f"You bought {item.title} with {count_elements} stickers for ${price}"
                                )
                        time.sleep(5)

                    except Exception:
                        time_now = datetime.datetime.now()
                        print(f"Page refresh error: {time_now}")
                        time.sleep(10)

        bot.polling()
