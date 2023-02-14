import yfinance as yf
import attrs_setter
import pandas as pd
def hex1_info():
    tick1 =yf.Ticker('HEX-USD')
    period1 = attrs_setter.period()
    interval1 = attrs_setter.interval()
    hex1_df = yf.download(tickers = "HEX-USD",period = period1,interval = interval1)
    pd.set_option("display.max.columns", None)
    pd.set_option("display.max.rows", None)
    return hex1_df

def hex1_ma():#calculates MA for ticker
    hex1_table = hex1_info()
    hex1_table['50MA'] = hex1_table.Close.rolling(50).mean()#calculates 50 day MA and puts in df
    hex1_table['200MA'] = hex1_table.Close.rolling(200).mean()#calculates 200 day MA and puts in df
    return hex1_table
