import requests

url = "https://api.marketdata.app/v1/options/quotes/AAPL250117C00150000/"

response = requests.request("GET", url)
data = response.json()

print("Option Contract: %s" % data["optionSymbol"][0])
print(data)

# -- Assignment -- #
# 1. Get the Ticker and current price of Ticker. URL: https://api.marketdata.app/v1/stocks/quotes/AAPL/
#   - Compare price from JSON and stock quotes API to real time price. May need to get live price from other API (alphavantage)
# 2. Get the Strike. Rule is to divide by 1000
# 3. Get the Expiration Date in the format: January 01, 2000


# 4. Get the Option Type (Call or Put)
# 5. Get Delta, Gamma, and Theta
# 6. Implement check for response code 200

# Code for #4, #5, #6

import requests  

url = "https://api.marketdata.app/v1/options/quotes/AAPL250117C00150000/"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Get the option type (call or put) from the 'side' field in JSON
    option_type = data["side"][0]

    # Retrieve the greek values from the JSON
    greeks = {
        "delta": data["delta"][0],
        "gamma": data["gamma"][0],
        "theta": data["theta"][0],
        "vega": data["vega"][0],
        "rho": data["rho"][0]
    }

    # Check if the response is valid based on the 's' field in JSON
    if data.get("s") == "ok":
        print(f"Option Type: {option_type}")
        print("Greek Values:")
        for key, value in greeks.items():
            print(f"{key}: {value}")
    else:
        print("Invalid response.")
else:
    print("Failed to retrieve data. Status code:", response.status_code)


