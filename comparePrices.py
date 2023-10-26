import requests, yfinance               # yfinance is not a default library, download if you haven't done so

tickers = ['AAPL', 'AMZN', 'MSFT', 'GOOGL', 'META', 'TSLA']

for ticker in tickers:
    # Get price and ticker from MarketData
    url = 'https://api.marketdata.app/v1/stocks/quotes/' + ticker
    mdQuote = requests.get(url, headers = {'Authorization' : 'Bearer ' + open('mdToken.txt', 'r').read()}).json()
    print(f'\nTicker: {mdQuote["symbol"][0]}')
    mdPrice = mdQuote["last"][0]
    print(f'MarketData Price: ${mdPrice:.2f}')

    # Get price from yfinance
    aapl = yfinance.Ticker(ticker)
    yfPrice = aapl.info['currentPrice']
    print(f'yfinance Price: ${yfPrice:.2f}')

    # Compare prices
    print(f'Prices differ by {mdPrice - yfPrice:.2f}')