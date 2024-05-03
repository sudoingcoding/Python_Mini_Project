import requests
import json

api_request=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=20&convert=USD&CMC_PRO_API_KEY=38478125-1faf-4c0f-8d41-8e08352f4c76")
api=json.loads(api_request.content)

coins = [
    {
        "symbol":"BTC",
        "amount_owned":2,
        "price_per_coin":3200    
    },
    {
        "symbol":"ETH",
        "amount_owned":100,
        "price_per_coin":2.05    
    }
]

for i in range(0,20):
    for coin in coins:
        if api["data"][i]["symbol"]==coin["symbol"]:
            print(api["data"][i]["name"]+"-"+api["data"][i]["symbol"])
            print("Price - ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
            print("---------------")

