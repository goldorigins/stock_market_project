import yfinance as yf
import attrs_setter
import pandas as pd
def axs_info():
    tick1 =yf.Ticker('AXS-USD')
    period1 = attrs_setter.period()
    interval1 = attrs_setter.interval()
    axs_df = yf.download(tickers = "AXS-USD",period = period1,interval = interval1)
    pd.set_option("display.max.columns", None)
    pd.set_option("display.max.rows", None)
    return axs_df

def axs_ma():#calculates MA for ticker
    axs_table = axs_info()
    axs_table['50MA'] = axs_table.Close.rolling(50).mean()#calculates 50 day MA and puts in df
    axs_table['200MA'] = axs_table.Close.rolling(200).mean()#calculates 200 day MA and puts in df
    return axs_table
