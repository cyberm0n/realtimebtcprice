import json
import requests

key = "https://api.binance.com/api/v3/ticker/price?symbol="
currencies = "BTCUSDT"

while True:
    url = key+currencies
    data = requests.get(url)
    data = data.json()
    with open('price.txt', 'a') as f:
        f.write(data+"\n")
    print(">>>",data)
