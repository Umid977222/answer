import requests
import time
from bs4 import BeautifulSoup

crypts = {'ETH_USDT': 1805, 'BTC_USDT': 1805}


def currency1():
    for key, val in crypts.items():
        if key == 'ETH_USDT':
            print(key, val)
            time.sleep(5)
            currency1()
        else:
            print('no crypts')


currency1()


'''Это простой ответ на ваших вопросов, 
ниже сделана небольшая программа  '''


# Crypto = 'https://alpari.com/ru/markets/crypto/'
# headers = {'User-Agent': 'Your User-agent'}
#
#
# def currency():
#     page = requests.get(Crypto, headers)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     crypto_top = soup.findAll("div", {"class": "-rdsn-card-markets-crypto__top"})
#     price = soup.findAll("p", {"class": "-rdsn-card-markets-crypto__price"})
#     print(f'Crypto:{crypto_top[1].text}Prices: {price[1].text}')
#     time.sleep(5)
#     currency()
#
#
# currency()
