import yfinance as yf
import attrs_setter
import pandas as pd
def bch_info():
    tick1 =yf.Ticker('BCH-USD')
    period1 = attrs_setter.period()
    interval1 = attrs_setter.interval()
    bch_df = yf.download(tickers = "BCH-USD",period = period1,interval = interval1)
    pd.set_option("display.max.columns", None)
    pd.set_option("display.max.rows", None)
    return bch_df

def bch_ma():#calculates MA for ticker
    bch_table = bch_info()
    bch_table['50MA'] = bch_table.Close.rolling(50).mean()#calculates 50 day MA and puts in df
    bch_table['200MA'] = bch_table.Close.rolling(200).mean()#calculates 200 day MA and puts in df
    return bch_table
