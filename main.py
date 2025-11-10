import requests
import pandas as pd
import matplotlib.pyplot as plt
import os

from datetime import datetime
import time

print("Running main.py...")

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

def transform_data(prices, vs_currency="usd"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = [
        {"coin": coin, "price": info[vs_currency], "currency": vs_currency, "timestamp": timestamp}
        for coin, info in prices.items()
    ]
    df = pd.DataFrame(data)
    return df

file_exists = os.path.isfile("coin_prices.csv")

raw_data = get_coin_price(["bitcoin", "ethereum", "dogecoin"])
df = transform_data(raw_data)
df.to_csv("coin_prices.csv", mode="a", header=not file_exists, index=False)
print("Saved new data point:", df)


'''
#while True:
    file_exists = os.path.isfile("coin_prices.csv")

    raw_data = get_coin_price(["bitcoin", "ethereum", "dogecoin"])
    df = transform_data(raw_data)
    df.to_csv("coin_prices.csv", mode="a", header=not file_exists, index=False)
    print("Saved new data point:", df)
    time.sleep(3600)  # every hour
'''
df = pd.read_csv("coin_prices.csv")
for coin in df['coin'].unique():
    plt.plot(df[df['coin'] == coin]['timestamp'], df[df['coin'] == coin]['price'], label=coin)
plt.legend()
plt.title("Crypto Prices Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Price (USD)")
plt.show()

'''
coins_to_fetch = ["bitcoin", "ethereum", "dogecoin"]
raw_data = get_coin_price(coins_to_fetch)
print(raw_data)

coin_list = ["bitcoin"]
data_list = get_coin_info(coin_list)
print(data_list)
'''





