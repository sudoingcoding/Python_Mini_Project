from tkinter import *
import requests
import json

pycrypto = Tk()
pycrypto.title("My Crypto Portfolio")

def my_portfolio():
    api_request=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=20&convert=USD&CMC_PRO_API_KEY=38478125-1faf-4c0f-8d41-8e08352f4c76")
    api=json.loads(api_request.content)

    coins = [
        {
            "symbol":"BTC",
            "amount_owned":2,
            "price_per_coin":3200    
        },
        {
            "symbol":"USDT",
            "amount_owned":10,
            "price_per_coin":20.05    
        },
        {
            "symbol":"ETH",
            "amount_owned":100,
            "price_per_coin":2.05     
        },
    ]
    total_pl=0
    coin_row=1
    
    for i in range(0,20):
        for coin in coins:
            if api["data"][i]["symbol"]==coin["symbol"]:
                total_paid=coin["amount_owned"]*coin["price_per_coin"]
                current_value=coin["amount_owned"]*api["data"][i]["quote"]["USD"]["price"]
                pl_percoin=api["data"][i]["quote"]["USD"]["price"]-coin["price_per_coin"]
                total_pl_coin=pl_percoin*coin["amount_owned"]
            
                total_pl+=total_pl_coin
            
                # print(api["data"][i]["name"]+" - "+api["data"][i]["symbol"])
                # print("Price - ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
                # print("Number Of Coin:",coin["price_per_coin"])
                # print("Total Amount Paid:","${0:.2f}".format(total_paid))
                # print("Current:","${0:.2f}".format(current_value))
                # print("P/L Per Coin:","${0:.2f}".format(pl_percoin))
                # print("Total P/L with Coin:","${0:.2f}".format(total_pl_coin))
                
                name = Label(pycrypto,text=api["data"][i]["symbol"],bg="black",fg="white") 
                name.grid(row=coin_row,column=0,sticky=N+S+E+W)

                Price = Label(pycrypto,text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]),bg="blue",fg="white") 
                Price.grid(row=coin_row,column=1,sticky=N+S+E+W)

                no_coins = Label(pycrypto,text=coin["price_per_coin"],bg="black",fg="white") 
                no_coins.grid(row=coin_row,column=2,sticky=N+S+E+W) 

                amount_paid = Label(pycrypto,text="${0:.2f}".format(total_paid),bg="blue",fg="white") 
                amount_paid.grid(row=coin_row,column=3,sticky=N+S+E+W) 


                current_val = Label(pycrypto,text="${0:.2f}".format(current_value),bg="black",fg="white") 
                current_val.grid(row=coin_row,column=4,sticky=N+S+E+W)

                pl_coin = Label(pycrypto,text="${0:.2f}".format(pl_percoin),bg="blue",fg="white") 
                pl_coin.grid(row=coin_row,column=5,sticky=N+S+E+W) 

                totalpl = Label(pycrypto,text="${0:.2f}".format(total_pl_coin),bg="black",fg="white") 
                totalpl.grid(row=coin_row,column=6,sticky=N+S+E+W) 

                coin_row+=1

    #print("Total P/L for Portfolio:","${0:.2f}".format(total_pl))

my_portfolio()

name = Label(pycrypto,text="Coin Name",bg="black",fg="white") 
name.grid(row=0,column=0,sticky=N+S+E+W)

Price = Label(pycrypto,text="Price",bg="blue",fg="white") 
Price.grid(row=0,column=1,sticky=N+S+E+W)

no_coins = Label(pycrypto,text="Coin Owned",bg="black",fg="white") 
no_coins.grid(row=0,column=2,sticky=N+S+E+W) 

amount_paid = Label(pycrypto,text="Total Amount Paid",bg="blue",fg="white") 
amount_paid.grid(row=0,column=3,sticky=N+S+E+W) 


current_val = Label(pycrypto,text="Current Value",bg="black",fg="white") 
current_val.grid(row=0,column=4,sticky=N+S+E+W)

pl_coin = Label(pycrypto,text="P/L Per Coin",bg="blue",fg="white") 
pl_coin.grid(row=0,column=5,sticky=N+S+E+W) 

totalpl = Label(pycrypto,text="Total P/L with Coin",bg="black",fg="white") 
totalpl.grid(row=0,column=6,sticky=N+S+E+W) 

pycrypto.mainloop()
print("Program Completed")