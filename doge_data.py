import yfinance as yf
import attrs_setter
import pandas as pd
def doge_info():
    tick1 =yf.Ticker('DOGE-USD')
    period1 = attrs_setter.period()
    interval1 = attrs_setter.interval()
    doge_df = yf.download(tickers = "DOGE-USD",period = period1,interval = interval1)
    pd.set_option("display.max.columns", None)
    pd.set_option("display.max.rows", None)
    return doge_df

def doge_ma():#calculates MA for ticker
    doge_table = doge_info()
    doge_table['50MA'] = doge_table.Close.rolling(50).mean()#calculates 50 day MA and puts in df
    doge_table['200MA'] = doge_table.Close.rolling(200).mean()#calculates 200 day MA and puts in df
    return doge_table
