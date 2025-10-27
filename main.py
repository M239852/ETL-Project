import requests

base_url = "https://api.coingecko.com/api/v3"


def get_coin_info(name):
    url = f"{base_url}/coins/list"
    response = requests.get(url)
    coins = response.json()
    if response.status_code != 200:
        print("Error fetching coin list")
        return
    else:
        print("Fetched coin list successfully")
    print(coins[:5])  # Print first 5 coins for reference

   




coin_name = "Bitcoin"
get_coin_info(coin_name)






