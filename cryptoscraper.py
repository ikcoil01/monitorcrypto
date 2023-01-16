from prometheus_client import start_http_server, Gauge
import random
import time
import requests
from bs4 import BeautifulSoup

def getcurrency(currencyName):
    # Define the URL of the website you want to scrape
    url = "https://www.coinmarketcap.com/currencies/" + currencyName + "/"

    # Use the requests library to fetch the HTML content of the website
    response = requests.get(url)
    html = response.text

    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(html, 'html.parser')

    # Find the element containing the cryptocurrency price
    price_element = soup.find('div', {'class': 'priceValue'})

    price = price_element.find('span').text.replace("$","")
    price = price.replace(",","")
    # Print the price
    print('The current price of '+currencyName+' is:', price)

    return price




crypto_symbols = ["bitcoin", "ethereum","tether","bnb","usd-coin","binance-usd","xrp","cardano","dogecoin"]
gauges = {}

for symbol in crypto_symbols:
    gauges[symbol] = Gauge(f'{symbol.replace("-","_")}_value', f'{symbol} value')
    gauges[symbol].set(float(getcurrency(symbol)))

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        for symbol in crypto_symbols:
            gauges[symbol].set(float(getcurrency(symbol)))
        time.sleep(30)



