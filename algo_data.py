import yfinance as yf
import attrs_setter
import pandas as pd
def algo_info():
    tick1 =yf.Ticker('ALGO-USD')
    period1 = attrs_setter.period()
    interval1 = attrs_setter.interval()
    algo_df = yf.download(tickers = "ALGO-USD",period = period1,interval = interval1)
    pd.set_option("display.max.columns", None)
    pd.set_option("display.max.rows", None)
    return algo_df

def algo_ma():#calculates MA for ticker
    algo_table = algo_info()
    algo_table['50MA'] = algo_table.Close.rolling(50).mean()#calculates 50 day MA and puts in df
    algo_table['200MA'] = algo_table.Close.rolling(200).mean()#calculates 200 day MA and puts in df
    return algo_table
