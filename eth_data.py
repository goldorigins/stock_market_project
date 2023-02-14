import yfinance as yf
import attrs_setter
import pandas as pd
def eth_info():
    tick1 =yf.Ticker('ETH-USD')
    period1 = attrs_setter.period()
    interval1 = attrs_setter.interval()
    eth_df = yf.download(tickers = "ETH-USD",period = period1,interval = interval1)
    pd.set_option("display.max.columns", None)
    pd.set_option("display.max.rows", None)
    return eth_df

def eth_ma():#calculates MA for ticker
    eth_table = eth_info()
    eth_table['50MA'] = eth_table.Close.rolling(50).mean()#calculates 50 day MA and puts in df
    eth_table['200MA'] = eth_table.Close.rolling(200).mean()#calculates 200 day MA and puts in df
    return eth_table
