import yfinance as yf
import attrs_setter
import pandas as pd
def usdt_info():
    tick1 =yf.Ticker('USDT-USD')
    period1 = attrs_setter.period()
    interval1 = attrs_setter.interval()
    usdt_df = yf.download(tickers = "USDT-USD",period = period1,interval = interval1)
    pd.set_option("display.max.columns", None)
    pd.set_option("display.max.rows", None)
    return usdt_df

def usdt_ma():#calculates MA for ticker
    usdt_table = usdt_info()
    usdt_table['50MA'] = usdt_table.Close.rolling(50).mean()#calculates 50 day MA and puts in df
    usdt_table['200MA'] = usdt_table.Close.rolling(200).mean()#calculates 200 day MA and puts in df
    return usdt_table
