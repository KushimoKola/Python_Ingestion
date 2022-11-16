# Run in terminal after setting up virtual envr - 
#python3 -m pip install schedule
#python3 -m pip install requests

import schedule # pip3 install schedule
import requests # pip3 install request
import time
import json

#having issues importing schedule and requests
  # Fixed, only had to run 'pip3 install request' in terminal

def pull_currency_data(site_url, apikey, file_name):
    """
    :param site_url: URL to which requests get should hit
    :param apikey: Key from your account
    :param file_name: location and file name where output should be saved/appended
    """
    global data
    data = requests.get(url=site_url+apikey)
    file = open(file_name, "a")
    currency = json.loads(data.content)
    output = data.headers['Date'] + '|' + '1' + '|' + str(currency['USD']) + '|' + str(currency['JPY']) + '|' + \
             str(currency['EUR']) + '|' + str(currency['NGN']) + '\n'
    file.write(output)
    file.close()

key = '2447285030a725a86d4ef48ea1336edb9c67189caa0750fb8ab4697799861dc8'
url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR,NGN&api_key='
file_name = './currency_extract.csv'

# Refresh rate is every 60seconds
schedule.every(60).seconds.do(pull_currency_data, url, key, file_name)

while True:
    schedule.run_pending()
    time.sleep(1)