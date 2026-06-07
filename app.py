# This function will get real time crypto currency data every day at 8 am (Specified time)
# this will also export data as csv file

# Dependencies
import requests
import schedule
import time
from datetime import datetime
import pandas as pd
from pathlib import Path

# getting crypto data
def get_crypto_data():
    # API Information
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    param = {
        'vs_currency' : 'usd',
        'order' : 'market_cap_desc', # to get highest crypto to lowest
        'per_page': 250, # adding more here will mark your ip as spam and block you
        'page': 1
    }

    # sending request
    response = requests.get(url, params=param)

    if response.status_code == 200:
        print("Connection Successful\nGetting the data...")

        # storing the response in data
        data = response.json()

        df = pd.DataFrame(data)

        # print(df.columns)
        # print(df.head())

        df = df[[
            'id', 
            'current_price', 
            'market_cap', 
            'price_change_percentage_24h',
            'ath',
            'atl' 
        ]]

        # creating new column
        today = datetime.now().strftime("%Y-%m-%d_%H-%M")
        df['time_stamp'] = today

        # negative top 10
        top_negative = df.sort_values(by='price_change_percentage_24h', ascending=True)
        top_negative_10 = top_negative.head(10)

        # positive top 10
        top_positive = df.sort_values(by='price_change_percentage_24h', ascending=False)
        top_positive_10 = top_positive.head(10)

        # saving data

        BASE_DIR = Path(__file__).resolve().parent
        OUTPUT_DIR = BASE_DIR / "output"
        OUTPUT_DIR.mkdir(exist_ok=True)

        output_file = OUTPUT_DIR / f"crypto_data_{today}.csv"

        output_file_positive_10 = OUTPUT_DIR / f"top_10_positive_of_{today}.csv"

        output_file_negative_10 = OUTPUT_DIR / f"top_10_negative_of_{today}.csv"

        top_negative_10.to_csv(output_file_negative_10, index=False)
        top_positive_10.to_csv(output_file_positive_10, index=False)
        df.to_csv(output_file, index=False)

        print("Data Saved Successfully!!")


    else:
        print(f'Connection Failed Error Code {response.status_code}')



# this get executed only if we run this function
if __name__ == '__main__':
    # call the function

    # sheduling the task at 8AM
    # schedule.every().day.at('08:00').do(get_crypto_data)
    schedule.every().day.at('17:59').do(get_crypto_data)
    
    while True:
        schedule.run_pending()
        time.sleep(60)