import requests
import pandas as pd
import time

def get_coin_twitter_handle(coin_id):
    url = f'https://api.coingecko.com/api/v3/coins/{coin_id}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        info = response.json()
        twitter_url = info['links'].get('twitter_screen_name')
        return twitter_url
    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 429:
            print("Rate limit exceeded. Waiting for 60 seconds.")
            time.sleep(60)
            return get_coin_twitter_handle(coin_id)
        else:
            print(err)
            return None
    except requests.exceptions.RequestException as e:
        print(e)
        return None

url = 'https://api.coingecko.com/api/v3/coins/list'
response = requests.get(url)
info = response.json()

data = []
for i, coin in enumerate(info):
    coin_id = coin['id']
    coin_name = coin['name']
    twitter_handle = get_coin_twitter_handle(coin_id)
    if twitter_handle:
        data.append([coin_name, twitter_handle])
    if (i + 1) % 100 == 0:
        print(f'Processed {i + 1} coins')
        df = pd.DataFrame(data, columns=['Coin Name', 'Twitter Handle'])
        df.to_excel('twitter_handles.xlsx', index=False)
    time.sleep(1.2)

df = pd.DataFrame(data, columns=['Coin Name', 'Twitter Handle'])
df.to_excel('twitter_handles.xlsx', index=False)

print("Total coin count with Twitter handle:", len(data))
