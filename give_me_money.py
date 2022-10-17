from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import config

options = webdriver.ChromeOptions()
options.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
)
options.add_extension('/home/yaroslav/projects/steam_bot/steam_bot/chromedriver/helper.crx')

class SteamBot(object):
    def __init__(self):
        self.driver = webdriver.Chrome(
                executable_path="../chromedriver/chromedriver",
                options=options
        )

    def buy_item(self, ind):
        # self.driver.find_element_by_id(
        #     'searchResultsRows'
        # ).find_elements_by_class_name('market_listing_buy_button')[0].click()
        self.driver.find_elements_by_class_name('market_listing_buy_button')[ind].click()
        print('try buy')
        self.driver.find_elements_by_xpath('//*[@id="market_buynow_dialog_accept_ssa"]')[0].click()
        self.driver.find_elements_by_xpath('//*[@id="market_buynow_dialog_purchase"]')[0].click()

    def check_name_tage(self):
        for ind, element in enumerate(
                self.driver.find_element_by_id(
                    'searchResultsRows'
                ).find_elements_by_class_name(
                    'market_listing_row'
                )[:5]
        ):
            if element.find_elements_by_class_name('sih-fraud'):
                self.buy_item(ind)
                print('Purchased item with name_tag')
                time.sleep(2)

    def login(self):
        self.driver.get(
            "https://store.steampowered.com/login/?redir=%3Fl%3Drussian&redir_ssl=1&snr=1_4_4__global-header"
        )
        time.sleep(30)

    def make_money(self):
        self.login()
        while True:
            print('New cycle')
            try:
                self.driver.get(config.P250_NP)
                self.check_name_tage()
                time.sleep(2)

                for ind, element in enumerate(self.driver.find_elements_by_xpath('//div[@class="sih-images"]')[:3]):
                    price = self.driver.find_elements_by_class_name('market_listing_their_price')[ind].text[1:5]
                    count_elements = len(element.find_elements_by_class_name('sticker-image'))
                    if count_elements == 4 and float(price) <= 0.80 or count_elements == 3 and float(price) <= 0.76:
                        self.buy_item(ind)
                        print('Purchased P250_NP with 4 stickers')
                        time.sleep(5)
                time.sleep(5)

            except Exception:
                print('Some Error')
                time.sleep(15)


            # new item
            try:
                self.driver.get(config.P250_PPI)
                self.check_name_tage()
                time.sleep(2)

                for ind, element in enumerate(self.driver.find_elements_by_xpath('//div[@class="sih-images"]')[:3]):
                    price = self.driver.find_elements_by_class_name('market_listing_their_price')[ind].text[1:5]
                    count_elements = len(element.find_elements_by_class_name('sticker-image'))
                    if count_elements == 4 and float(price) <= 0.58 or count_elements == 3 and float(price) <= 0.55:
                        self.buy_item(ind)
                        print('Purchased P250_NP with 4 stickers')
                        time.sleep(5)
                time.sleep(5)

            except Exception:
                print('Some Error')
                time.sleep(15)

            # new item
            try:
                self.driver.get(config.MP9_PPI)
                self.check_name_tage()
                time.sleep(2)
                for ind, element in enumerate(self.driver.find_elements_by_xpath('//div[@class="sih-images"]')[:3]):
                    price = self.driver.find_elements_by_class_name('market_listing_their_price')[ind].text[1:5]
                    count_elements = len(element.find_elements_by_class_name('sticker-image'))
                    if count_elements == 4 and float(price) <= 1.10 or count_elements == 3 and float(price) <= 1.07:
                        self.buy_item(ind)
                        print('Purchased P250_NP with 4 stickers')
                        time.sleep(5)
                time.sleep(5)
            except Exception:
                print('Some Error')
                time.sleep(15)

            # new item
            try:
                self.driver.get(config.Tec9_NP)
                self.check_name_tage()
                time.sleep(2)
                for ind, element in enumerate(self.driver.find_elements_by_xpath('//div[@class="sih-images"]')[:3]):
                    price = self.driver.find_elements_by_class_name('market_listing_their_price')[ind].text[1:5]
                    count_elements = len(element.find_elements_by_class_name('sticker-image'))
                    if count_elements == 4 and float(price) <= 0.82:
                        self.buy_item(ind)
                        print('Purchased Tec-9 with 4 stickers')
                        time.sleep(5)
                time.sleep(5)
            except Exception:
                print('Some Error')
                time.sleep(15)

            #new item
            try:
                self.driver.get('https://steamcommunity.com/market/listings/730/AWP%20%7C%20Exoskeleton%20%28Field-Tested%29')
                self.check_name_tage()
                time.sleep(2)
                for ind, element in enumerate(self.driver.find_elements_by_xpath('//div[@class="sih-images"]')[:3]):
                    price = self.driver.find_elements_by_class_name('market_listing_their_price')[ind].text[1:5]
                    count_elements = len(element.find_elements_by_class_name('sticker-image'))
                    if count_elements == 4 and float(price) <= 1.55:
                        self.buy_item(ind)
                        print('Purchased TEST1 with 4 stickers')
                        time.sleep(5)
                time.sleep(5)
            except Exception:
                print('Some Error')
                time.sleep(15)

            #new item
            try:
                self.driver.get(
                    'https://steamcommunity.com/market/listings/730/CZ75-Auto%20%7C%20Red%20Astor%20%28Minimal%20Wear%29')
                self.check_name_tage()
                time.sleep(2)
                for ind, element in enumerate(self.driver.find_elements_by_xpath('//div[@class="sih-images"]')[:3]):
                    price = self.driver.find_elements_by_class_name('market_listing_their_price')[ind].text[1:5]
                    count_elements = len(element.find_elements_by_class_name('sticker-image'))
                    if count_elements == 4 and float(price) <= 0.76:
                        self.buy_item(ind)
                        print('Purchased TEST2 with 4 stickers')
                        time.sleep(5)
                time.sleep(5)
            except Exception:
                print('Some Error')
                time.sleep(15)

            #new item
            try:
                self.driver.get(config.SSG08_PPI)
                self.check_name_tage()
                time.sleep(5)
                # for ind, element in enumerate(self.driver.find_elements_by_xpath('//div[@class="sih-images"]')[:3]):
                #     price = self.driver.find_elements_by_class_name('market_listing_their_price')[ind].text[1:5]
                #     count_elements = len(element.find_elements_by_class_name('sticker-image'))
                #     if count_elements == 4 and float(price) <= 0.55:
                #         self.buy_item(ind)
                #         print('Purchased SSG08_PPI with 4 stickers')
                #         time.sleep(5)
                # time.sleep(10)
            except Exception:
                print('Some Error')
                time.sleep(15)

if __name__ == '__main__':
    bot = SteamBot()
    bot.make_money()








