import requests
import pandas as pd

url = 'https://api.coingecko.com/api/v3/coins/list'

response = requests.get(url)
info = response.json()

coins = []
for coin in info:
    coins.append(coin['name'])

df = pd.DataFrame(coins, columns=['Coin Name'])

df.to_excel('coins.xlsx', index=False)

print(df)

print("Total coin count:", len(coins))
