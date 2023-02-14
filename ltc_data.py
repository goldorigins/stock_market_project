import yfinance as yf
import attrs_setter
import pandas as pd
def ltc_info():
    tick1 =yf.Ticker('LTC-USD')
    period1 = attrs_setter.period()
    interval1 = attrs_setter.interval()
    ltc_df = yf.download(tickers = "LTC-USD",period = period1,interval = interval1)
    pd.set_option("display.max.columns", None)
    pd.set_option("display.max.rows", None)
    return ltc_df

def ltc_ma():#calculates MA for ticker
    ltc_table = ltc_info()
    ltc_table['50MA'] = ltc_table.Close.rolling(50).mean()#calculates 50 day MA and puts in df
    ltc_table['200MA'] = ltc_table.Close.rolling(200).mean()#calculates 200 day MA and puts in df
    return ltc_table
