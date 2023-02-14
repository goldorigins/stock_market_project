import yfinance as yf
import attrs_setter
import pandas as pd
def avax_info():
    tick1 =yf.Ticker('AVAX-USD')
    period1 = attrs_setter.period()
    interval1 = attrs_setter.interval()
    avax_df = yf.download(tickers = "AVAX-USD",period = period1,interval = interval1)
    pd.set_option("display.max.columns", None)
    pd.set_option("display.max.rows", None)
    return avax_df

def avax_ma():#calculates MA for ticker
    avax_table = avax_info()
    avax_table['50MA'] = avax_table.Close.rolling(50).mean()#calculates 50 day MA and puts in df
    avax_table['200MA'] = avax_table.Close.rolling(200).mean()#calculates 200 day MA and puts in df
    return avax_table
