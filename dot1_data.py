import yfinance as yf
import attrs_setter
import pandas as pd
def dot1_info():
    tick1 =yf.Ticker('DOT1-USD')
    period1 = attrs_setter.period()
    interval1 = attrs_setter.interval()
    dot1_df = yf.download(tickers = "DOT1-USD",period = period1,interval = interval1)
    pd.set_option("display.max.columns", None)
    pd.set_option("display.max.rows", None)
    return dot1_df

def dot1_ma():#calculates MA for ticker
    dot1_table = dot1_info()
    dot1_table['50MA'] = dot1_table.Close.rolling(50).mean()#calculates 50 day MA and puts in df
    dot1_table['200MA'] = dot1_table.Close.rolling(200).mean()#calculates 200 day MA and puts in df
    return dot1_table
