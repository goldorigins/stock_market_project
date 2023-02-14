import yfinance as yf
import attrs_setter
import pandas as pd
def vet_info():
    tick1 =yf.Ticker('VET-USD')
    period1 = attrs_setter.period()
    interval1 = attrs_setter.interval()
    vet_df = yf.download(tickers = "VET-USD",period = period1,interval = interval1)
    pd.set_option("display.max.columns", None)
    pd.set_option("display.max.rows", None)
    return vet_df

def vet_ma():#calculates MA for ticker
    vet_table = vet_info()
    vet_table['50MA'] = vet_table.Close.rolling(50).mean()#calculates 50 day MA and puts in df
    vet_table['200MA'] = vet_table.Close.rolling(200).mean()#calculates 200 day MA and puts in df
    return vet_table
