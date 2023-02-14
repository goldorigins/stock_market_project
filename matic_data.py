import yfinance as yf
import attrs_setter
import pandas as pd
def matic_info():
    tick1 =yf.Ticker('MATIC-USD')
    period1 = attrs_setter.period()
    interval1 = attrs_setter.interval()
    matic_df = yf.download(tickers = "MATIC-USD",period = period1,interval = interval1)
    pd.set_option("display.max.columns", None)
    pd.set_option("display.max.rows", None)
    return matic_df

def matic_ma():#calculates MA for ticker
    matic_table = matic_info()
    matic_table['50MA'] = matic_table.Close.rolling(50).mean()#calculates 50 day MA and puts in df
    matic_table['200MA'] = matic_table.Close.rolling(200).mean()#calculates 200 day MA and puts in df
    return matic_table
