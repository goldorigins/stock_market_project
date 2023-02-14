import yfinance as yf
import attrs_setter
import pandas as pd
def luna1_info():
    tick1 =yf.Ticker('LUNA1-USD')
    period1 = attrs_setter.period()
    interval1 = attrs_setter.interval()
    luna1_df = yf.download(tickers = "LUNA1-USD",period = period1,interval = interval1)
    pd.set_option("display.max.columns", None)
    pd.set_option("display.max.rows", None)
    return luna1_df

def luna1_ma():#calculates MA for ticker
    luna1_table = luna1_info()
    luna1_table['50MA'] = luna1_table.Close.rolling(50).mean()#calculates 50 day MA and puts in df
    luna1_table['200MA'] = luna1_table.Close.rolling(200).mean()#calculates 200 day MA and puts in df
    return luna1_table
