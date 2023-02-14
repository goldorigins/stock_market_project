import yfinance as yf
import attrs_setter
import pandas as pd
def link_info():
    tick1 =yf.Ticker('LINK-USD')
    period1 = attrs_setter.period()
    interval1 = attrs_setter.interval()
    link_df = yf.download(tickers = "LINK-USD",period = period1,interval = interval1)
    pd.set_option("display.max.columns", None)
    pd.set_option("display.max.rows", None)
    return link_df

def link_ma():#calculates MA for ticker
    link_table = link_info()
    link_table['50MA'] = link_table.Close.rolling(50).mean()#calculates 50 day MA and puts in df
    link_table['200MA'] = link_table.Close.rolling(200).mean()#calculates 200 day MA and puts in df
    return link_table
