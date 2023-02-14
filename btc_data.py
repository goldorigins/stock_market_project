import yfinance as yf
import attrs_setter
import pandas as pd
def btc_info():
    tick1 =yf.Ticker('BTC-USD')
    period1 = attrs_setter.period()
    interval1 = attrs_setter.interval()
    btc_df = yf.download(tickers = "BTC-USD",period = period1,interval = interval1)
    pd.set_option("display.max.columns", None)
    pd.set_option("display.max.rows", None)
    return btc_df

def btc_ma():#calculates MA for ticker
    btc_table = btc_info()
    btc_table['50MA'] = btc_table.Close.rolling(50).mean()#calculates 50 day MA and puts in df
    btc_table['200MA'] = btc_table.Close.rolling(200).mean()#calculates 200 day MA and puts in df
    return btc_table



