import yfinance as yf
import attrs_setter
import pandas as pd
def icp1_info():
    tick1 =yf.Ticker('ICP1-USD')
    period1 = attrs_setter.period()
    interval1 = attrs_setter.interval()
    icp1_df = yf.download(tickers = "ICP1-USD",period = period1,interval = interval1)
    pd.set_option("display.max.columns", None)
    pd.set_option("display.max.rows", None)
    return icp1_df

def icp1_ma():#calculates MA for ticker
    icp1_table = icp1_info()
    icp1_table['50MA'] = icp1_table.Close.rolling(50).mean()#calculates 50 day MA and puts in df
    icp1_table['200MA'] = icp1_table.Close.rolling(200).mean()#calculates 200 day MA and puts in df
    return icp1_table
