import yfinance as yf
import attrs_setter
import pandas as pd
def atom1_info():
    tick1 =yf.Ticker('ATOM1-USD')
    period1 = attrs_setter.period()
    interval1 = attrs_setter.interval()
    atom1_df = yf.download(tickers = "ATOM1-USD",period = period1,interval = interval1)
    pd.set_option("display.max.columns", None)
    pd.set_option("display.max.rows", None)
    return atom1_df

def atom1_ma():#calculates MA for ticker
    atom1_table = atom1_info()
    atom1_table['50MA'] = atom1_table.Close.rolling(50).mean()#calculates 50 day MA and puts in df
    atom1_table['200MA'] = atom1_table.Close.rolling(200).mean()#calculates 200 day MA and puts in df
    return atom1_table
