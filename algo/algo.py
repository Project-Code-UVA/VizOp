import requests, format_date, yfinance as yf

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
    mdPrice = response.json()['mid'][0]
    print(f'{ticker} MarketData Price for: ${mdPrice:.2f}')

#Get option contract data
url = "https://api.marketdata.app/v1/options/quotes/AAPL250117C00150000/"

response = requests.request("GET", url)
data = response.json()

if response.status_code == 200:
    data = response.json()
    if data.get("s") == "ok":    # Check if the response is valid based on the 's' field in JSON

        option_type = data["side"][0] # Call or Put
        strike = data['strike'][0] # Strike price of contract
        print("Option Contract: %s" % data["optionSymbol"][0])
        print(format_date.epoch_to_datetime(data['expiration'][0]))
        print("Strike: %s" % strike)

        greeks = { # Delta, Gamma, Theta, Vega, Rho
            "delta": data["delta"][0],
            "gamma": data["gamma"][0],
            "theta": data["theta"][0],
            "vega": data["vega"][0],
            "rho": data["rho"][0]
        }

        print(f"Option Type: {option_type}")
        print("Greek Values:")
        for key, value in greeks.items():
            print(f"{key}: {value}")

        print("Raw JSON Data:")
        print(data)

    else:
        print("Invalid response.")
    
else:
    print("Failed to retrieve data. Status code:", response.status_code)

price_range = (mdPrice - mdPrice * 0.1, mdPrice + mdPrice * 0.1)
delta = greeks['delta'] 
gamma = greeks['theta']
buy_premium = data['bid'][0]


#calculation premiums for call options
end_premiums = []
for end_price in range(int(price_range[0]), int(price_range[1])):
    end_price = round(end_price / 100, 2)
    change_in_price = end_price - mdPrice
    change_in_premium = change_in_price * delta + 0.5 * gamma * (change_in_price ** 2)
    end_premiums.append(change_in_premium + buy_premium)

print(end_premiums)

import matplotlib.pyplot as plt

plt.plot(range(mdPrice, price_range[1], 0.01), end_premiums)
plt.title(data["optionSymbol"][0])
plt.xlabel('Price Range')
plt.ylabel('End Premiums')
plt.show()
