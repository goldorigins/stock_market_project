import yfinance as yf
import attrs_setter
import pandas as pd
def bnb_info():
    tick1 =yf.Ticker('BNB-USD')
    period1 = attrs_setter.period()
    interval1 = attrs_setter.interval()
    bnb_df = yf.download(tickers = "BNB-USD",period = period1,interval = interval1)
    pd.set_option("display.max.columns", None)
    pd.set_option("display.max.rows", None)
    return bnb_df

def bnb_ma():#calculates MA for ticker
    bnb_table = bnb_info()
    bnb_table['50MA'] = bnb_table.Close.rolling(50).mean()#calculates 50 day MA and puts in df
    bnb_table['200MA'] = bnb_table.Close.rolling(200).mean()#calculates 200 day MA and puts in df
    return bnb_table
