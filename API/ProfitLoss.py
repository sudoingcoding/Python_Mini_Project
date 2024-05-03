import requests
import json

api_request=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=20&convert=USD&CMC_PRO_API_KEY=38478125-1faf-4c0f-8d41-8e08352f4c76")
api=json.loads(api_request.content)

print("---------------")
print("---------------")

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
total_pl=0

for i in range(0,20):
    for coin in coins:
        if api["data"][i]["symbol"]==coin["symbol"]:
            total_paid=coin["amount_owned"]*coin["price_per_coin"]
            current_value=coin["amount_owned"]*api["data"][i]["quote"]["USD"]["price"]
            pl_percoin=api["data"][i]["quote"]["USD"]["price"]-coin["price_per_coin"]
            total_pl_coin=pl_percoin*coin["amount_owned"]
            
            total_pl+=total_pl_coin
            
            print(api["data"][i]["name"]+" - "+api["data"][i]["symbol"])
            print("Price - ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
            print("Number Of Coin:",coin["price_per_coin"])
            print("Total Amount Paid:","${0:.2f}".format(total_paid))
            print("Current:","${0:.2f}".format(current_value))
            print("P/L Per Coin:","${0:.2f}".format(pl_percoin))
            print("Total P/L with Coin:","${0:.2f}".format(total_pl_coin))
            


            print("---------------")

print("Total P/L for Portfolio:","${0:.2f}".format(total_pl))
