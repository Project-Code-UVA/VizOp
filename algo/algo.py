import requests, format_date


url = "https://api.marketdata.app/v1/options/quotes/AAPL250117C00150000/"

response = requests.request("GET", url)
data = response.json()

strike = data['strike'][0]
print("Option Contract: %s" % data["optionSymbol"][0])
print(format_date.epoch_to_datetime(data['expiration'][0]))
print(data)


# -- Assignment -- #
# 1. Get the Ticker and current price of Ticker. URL: https://api.marketdata.app/v1/stocks/quotes/AAPL/
#   - Compare price from JSON and stock quotes API to real time price. May need to get live price from other API (alphavantage)
# 2. Get the Strike. Rule is to divide by 1000
# 3. Get the Expiration Date in the format: January 01, 2000
# 4. Get the Option Type (Call or Put)
# 5. Get Delta, Gamma, and Theta
# 6. Implement check for response code 200



