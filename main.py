import requests
import pandas
from datetime import datetime


# CoinGecko API base URL
base_url = "https://api.coingecko.com/api/v3"

# Function to get coin information by name
def get_coin_info(name):
    url = f"{base_url}/coins/list"
    response = requests.get(url)
    coins = response.json()
    if response.status_code != 200:
        print("Error fetching coin list")
        return
    else:
        print("Fetched coin list successfully")
    print(coins[:10])  # Print first 10 coins for reference

def get_coin_price(coin_ids, vs_currency="usd"):
    ids = ",".join(coin_ids)
    url = f"{base_url}/simple/price?ids={ids}&vs_currencies={vs_currency}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error fetching coin prices")
        return
    else:
        print("Fetched coin prices successfully")
        prices = response.json()
    return prices
   

# example usage
coins_to_fetch = ["bitcoin", "ethereum", "dogecoin"]
raw_data = get_coin_price(coins_to_fetch)
print(raw_data)





