import yfinance as yf
import attrs_setter
import pandas as pd
def uni3_info():
    tick1 =yf.Ticker('UNI3-USD')
    period1 = attrs_setter.period()
    interval1 = attrs_setter.interval()
    uni3_df = yf.download(tickers = "UNI3-USD",period = period1,interval = interval1)
    pd.set_option("display.max.columns", None)
    pd.set_option("display.max.rows", None)
    return uni3_df

def uni3_ma():#calculates MA for ticker
    uni3_table = uni3_info()
    uni3_table['50MA'] = uni3_table.Close.rolling(50).mean()#calculates 50 day MA and puts in df
    uni3_table['200MA'] = uni3_table.Close.rolling(200).mean()#calculates 200 day MA and puts in df
    return uni3_table
