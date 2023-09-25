import datetime
import time

import telebot
from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from apps.items import utils
from apps.items.models import Item
from apps.items.utils import token

options = webdriver.ChromeOptions()
options.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
)
options.add_extension('/Users/mac/PycharmProjects/steam_bot/easy_money/chromedriver/helper.crx')
driver = webdriver.Chrome(options=options)


class Command(BaseCommand):
    def handle(self, *args, **options):
        bot = telebot.TeleBot(token)
        driver.get(utils.login_url)
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.newlogindialog_TextInput_2eKVn[value=""]'))
        )
        driver.find_element(
            By.CSS_SELECTOR, '.newlogindialog_TextInput_2eKVn[value=""]'
        ).send_keys(utils.USERNAME)
        time.sleep(1)

        driver.find_element(
            By.CSS_SELECTOR, '.newlogindialog_TextInput_2eKVn[type="password"]'
        ).send_keys(utils.PASSWORD)

        driver.find_element(By.CSS_SELECTOR, 'button.newlogindialog_SubmitButton_2QgFE[type="submit"]')


        @bot.message_handler(commands=['start'])
        def send_text_name_tag(message):
            balance = 0
            while True:
                for item in Item.objects.filter(is_active=True):
                    try:
                        driver.get(item.link)
                        get_balance = float(driver.find_elements_by_id('marketWalletBalanceAmount')[0].text[1:])
                        if get_balance > balance:
                            profit = get_balance - balance
                            balance = get_balance
                            bot.send_message(
                                message.chat.id,
                                f"Your balance has increased by: ${round(profit, 2)} and is now ${balance}"
                            )
                        for ind, element in enumerate(
                                driver.find_element_by_id('searchResultsRows').find_elements_by_class_name(
                                    'market_listing_row')[:5]
                        ):
                            price = driver.find_elements_by_class_name('market_listing_their_price')[ind].text[1:5]
                            if element.find_elements_by_class_name('sih-fraud') and float(price) <= item.price_for_name_tag:
                                driver.find_elements_by_class_name('market_listing_buy_button')[ind].click()
                                print('try buy')
                                driver.find_elements_by_xpath('//*[@id="market_buynow_dialog_accept_ssa"]')[0].click()
                                driver.find_elements_by_xpath('//*[@id="market_buynow_dialog_purchase"]')[0].click()
                                balance = balance - float(price)
                                item_image = open(
                                    f"{utils.abs_url}{item.image}",
                                    "rb"
                                )
                                bot.send_message(
                                    message.chat.id,
                                    f"You've bought {item.title} with a name tag for ${price}"
                                )
                                bot.send_photo(
                                    message.chat.id, item_image
                                )
                        time.sleep(2)
                        if item.price_4:
                            for ind, element in enumerate(driver.find_elements_by_xpath('//div[@class="sih-images"]')[:4]):
                                price = driver.find_elements_by_class_name('market_listing_their_price')[ind].text[1:5]
                                count_elements = len(element.find_elements_by_class_name('sticker-image'))
                                if count_elements == 4 and float(price) <= item.price_4:
                                    driver.find_elements_by_class_name('market_listing_buy_button')[ind].click()
                                    print('try buy')
                                    driver.find_elements_by_xpath('//*[@id="market_buynow_dialog_accept_ssa"]')[0].click()
                                    driver.find_elements_by_xpath('//*[@id="market_buynow_dialog_purchase"]')[0].click()
                                    balance = balance - float(price)
                                    item_image = open(
                                        f"/home/yaroslav/projects/steam_bot/steam_bot/easy_money/config/media/{item.image}",
                                        "rb"
                                    )
                                    bot.send_message(
                                        message.chat.id,
                                        f"You've bought {item.title} with {count_elements} stickers for ${price}"
                                    )
                                    bot.send_photo(
                                        message.chat.id, item_image
                                    )
                            time.sleep(3)

                    except Exception:
                        time_now = datetime.datetime.now()
                        print(f"Page refresh error: {time_now}")
                        time.sleep(10)

        bot.polling()