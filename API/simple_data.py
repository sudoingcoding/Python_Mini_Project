import requests
import json

api_request=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=2&convert=USD&CMC_PRO_API_KEY=38478125-1faf-4c0f-8d41-8e08352f4c76")
api=json.loads(api_request.content)

print(api["data"][0]["symbol"])
print(api["data"][0]["quote"]["USD"]["price"])