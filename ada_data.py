import yfinance as yf
import attrs_setter
import pandas as pd
def ada_info():
    tick1 =yf.Ticker('ADA-USD')
    period1 = attrs_setter.period()
    interval1 = attrs_setter.interval()
    ada_df = yf.download(tickers = "ADA-USD",period = period1,interval = interval1)
    pd.set_option("display.max.columns", None)
    pd.set_option("display.max.rows", None)
    return ada_df

def ada_ma():#calculates MA for ticker
    ada_table = ada_info()
    ada_table['50MA'] = ada_table.Close.rolling(50).mean()#calculates 50 day MA and puts in df
    ada_table['200MA'] = ada_table.Close.rolling(200).mean()#calculates 200 day MA and puts in df
    return ada_table
