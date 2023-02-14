import yfinance as yf

tick1 =yf.Ticker('DOGE-USD')

df = yf.download(
tickers = "DOGE-USD",
period = "7d",
interval = "1m"
)
print(df)
