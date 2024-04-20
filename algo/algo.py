import requests, format_date, yfinance as yf
import options_algo
import pandas as pd

#compare prices of ticker from yfinance and MarketData
## !--- NEED TO GET TOKEN FOR TICKERS OTHER THAN AAPL ---! ##

tickers = ['AAPL'] 

for ticker in tickers:
    # Get price and ticker from MarketData
    live_price_url = 'https://api.marketdata.app/v1/stocks/quotes/' + ticker
    # mdQuote = requests.get(live_price_url, headers = {'Authorization' : 'Bearer ' + open('mdToken.txt', 'r').read()}).json()
    # print(f'\nTicker: {mdQuote["symbol"][0]}')
    # mdPrice = mdQuote["last"][0]

    response = requests.request("GET", live_price_url)
    mdPrice = response.json()['ask'][0]

#Get option contract data
url = "https://api.marketdata.app/v1/options/quotes/AAPL250117C00150000/"

response = requests.request("GET", url)
data = response.json()

if response.status_code == 200:
    data = response.json()
    if data.get("s") == "ok":    # Check if the response is valid based on the 's' field in JSON

        option_type = data["side"][0] # Call or Put
        strike = data['strike'][0] # Strike price of contract

        greeks = { # Delta, Gamma, Theta, Vega, Rho
            "delta": data["delta"][0],
            "gamma": data["gamma"][0],
            "theta": data["theta"][0],
            "vega": data["vega"][0],
            "rho": data["rho"][0]
        }

        print("Raw JSON Data:")
        print(data)

    else:
        print("Invalid response.")
    
else:
    print("Failed to retrieve data. Status code:", response.status_code)

# price_range = (mdPrice - mdPrice * 0.1, mdPrice + mdPrice * 0.1)
delta = greeks['delta'] 
gamma = greeks['theta']
theta = abs(greeks['theta'])
theta = 1.00
buy_premium = data['ask'][0]
mdPrice = data['underlyingPrice'][0]
print(mdPrice)
print(buy_premium)
date = pd.Timestamp.today()
x, y, z = options_algo.generate_data(buy_premium, delta, gamma, theta, date, mdPrice)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# ax.scatter(x, y, z, c=z, cmap='viridis')
ax.plot_trisurf(x, y, z, cmap='viridis', edgecolor='none')

ax.set_xlabel('Time')
ax.set_ylabel('Price')
ax.set_zlabel('New Premium')

plt.show()