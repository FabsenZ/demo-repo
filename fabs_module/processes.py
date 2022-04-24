import yfinance as yf


print('==============')
ticker = "AAPL"
stock_data = yf.download(ticker, start='2021-01-02', end="2021-01-31")
print(ticker, '==> NOT IN Method')


def get_ticker_data():
    msft = yf.Ticker("MSFT")
    print(msft.info
    )
    print(type(msft))
    print("CODE HAT FUNKTIONIERT")

