import yfinance as yf
import attrs_setter
import pandas as pd
def shib_info():
    tick1 =yf.Ticker('SHIB-USD')
    period1 = attrs_setter.period()
    interval1 = attrs_setter.interval()
    shib_df = yf.download(tickers = "SHIB-USD",period = period1,interval = interval1)
    pd.set_option("display.max.columns", None)
    pd.set_option("display.max.rows", None)
    return shib_df

def shib_ma():#calculates MA for ticker
    shib_table = shib_info()
    shib_table['50MA'] = shib_table.Close.rolling(50).mean()#calculates 50 day MA and puts in df
    shib_table['200MA'] = shib_table.Close.rolling(200).mean()#calculates 200 day MA and puts in df
    return shib_table
