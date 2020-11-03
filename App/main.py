import time
import requests
from bs4 import BeautifulSoup

class Currency:
    dollar = "https://www.google.ru/search?newwindow=1&sxsrf=ALeKk01lQ3k2Xh5HLGv3lHTFb4POomIi-Q%3A1604357995890&source=hp&ei=a4-gX_PkM-v2qwGe44bIDA&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83&gs_lcp=CgZwc3ktYWIQAxgAMg0IABCxAxCDARBGEIICMgIIADICCAAyCAgAELEDEIMBMgIIADICCAAyAggAMgIIADICCAAyAggAOgoIABCxAxCDARAKOggIABAKEAEQKjoGCAAQChABOgQIABAKOgIILjoKCC4Q6gIQJxCTAjoHCC4Q6gIQJzoHCCMQ6gIQJzoFCAAQsQM6CAguELEDEJMCOgUILhCxA1DjDFjNOmD-SGgDcAB4AYABuwGIAekKkgEDOS41mAEAoAEBqgEHZ3dzLXdperABCg&sclient=psy-ab"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
    converted_price = 0
    difference = 5
    time_min = 5

    def __init__(self):
        self.converted_price = float(self.get_currensy_price().replace(",", "."))

    def get_currensy_price(self):
        full_page = requests.get(self.dollar, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
        return convert[0].text

    def check_currency(self):
        currency = float(self.get_currensy_price().replace(",", "."))
        if currency >= self.converted_price + self.difference:
            print("Курс сильно вырос!!!")
        elif currency <= self.converted_price - self.difference:
            print("Курс сильно упал!!!")
        print("Сейчас доллар: " + str(currency))
        time.sleep(self.time_min)
        self.check_currency()

currency_doll = Currency()
currency_doll.check_currency()

