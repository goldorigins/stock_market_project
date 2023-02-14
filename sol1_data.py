import yfinance as yf
import attrs_setter
import pandas as pd
def sol1_info():
    tick1 =yf.Ticker('SOL1-USD')
    period1 = attrs_setter.period()
    interval1 = attrs_setter.interval()
    sol1_df = yf.download(tickers = "SOL1-USD",period = period1,interval = interval1)
    pd.set_option("display.max.columns", None)
    pd.set_option("display.max.rows", None)
    return sol1_df

def sol1_ma():#calculates MA for ticker
    sol1_table = sol1_info()
    sol1_table['50MA'] = sol1_table.Close.rolling(50).mean()#calculates 50 day MA and puts in df
    sol1_table['200MA'] = sol1_table.Close.rolling(200).mean()#calculates 200 day MA and puts in df
    return sol1_table
