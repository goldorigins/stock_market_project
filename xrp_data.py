import yfinance as yf
import attrs_setter
import pandas as pd
def xrp_info():
    tick1 =yf.Ticker('XRP-USD')
    period1 = attrs_setter.period()
    interval1 = attrs_setter.interval()
    xrp_df = yf.download(tickers = "XRP-USD",period = period1,interval = interval1)
    pd.set_option("display.max.columns", None)
    pd.set_option("display.max.rows", None)
    return xrp_df

def xrp_ma():#calculates MA for ticker
    xrp_table = xrp_info()
    xrp_table['50MA'] = xrp_table.Close.rolling(50).mean()#calculates 50 day MA and puts in df
    xrp_table['200MA'] = xrp_table.Close.rolling(200).mean()#calculates 200 day MA and puts in df
    return xrp_table
