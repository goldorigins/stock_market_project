import yfinance as yf
import attrs_setter
import pandas as pd
def xlm_info():
    tick1 =yf.Ticker('XLM-USD')
    period1 = attrs_setter.period()
    interval1 = attrs_setter.interval()
    xlm_df = yf.download(tickers = "XLM-USD",period = period1,interval = interval1)
    pd.set_option("display.max.columns", None)
    pd.set_option("display.max.rows", None)
    return xlm_df

def xlm_ma():#calculates MA for ticker
    xlm_table = xlm_info()
    xlm_table['50MA'] = xlm_table.Close.rolling(50).mean()#calculates 50 day MA and puts in df
    xlm_table['200MA'] = xlm_table.Close.rolling(200).mean()#calculates 200 day MA and puts in df
    return xlm_table
