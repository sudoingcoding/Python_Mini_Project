import requests
import json

api_request=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=38478125-1faf-4c0f-8d41-8e08352f4c76")
api=json.loads(api_request.content)

coins = ["BTC","ETH"]

for i in range(0,5):
    for coin in coins:
        if api["data"][i]["symbol"]==coin:
            print(api["data"][i]["symbol"])
            print("{0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
            print("---------------")

