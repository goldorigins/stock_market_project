import yfinance as yf
import attrs_setter
import pandas as pd
def usdc_info():
    tick1 =yf.Ticker('USDC-USD')
    period1 = attrs_setter.period()
    interval1 = attrs_setter.interval()
    usdc_df = yf.download(tickers = "USDC-USD",period = period1,interval = interval1)
    pd.set_option("display.max.columns", None)
    pd.set_option("display.max.rows", None)
    return usdc_df

def usdc_ma():#calculates MA for ticker
    usdc_table = usdc_info()
    usdc_table['50MA'] = usdc_table.Close.rolling(50).mean()#calculates 50 day MA and puts in df
    usdc_table['200MA'] = usdc_table.Close.rolling(200).mean()#calculates 200 day MA and puts in df
    return usdc_table
