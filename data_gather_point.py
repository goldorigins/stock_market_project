import btc_data
import doge_data
import bnb_data
import eth_data
import pandas as pd
#bring the variables in.
#eache var is a pandas df of yahoo fincance data
global bnb
global btc
global doge
global eth
#bnb = bnb_data.bnb_ma()
btc = btc_data.btc_ma()
#doge = doge_data.doge_ma()
#eth = eth_data.eth_ma()
#dont forget to add your ticker to the list
global ticker_list

def data_cutter(): #cuts of extra data for easy handling
    btc.drop(btc.index[1:8700], inplace = True)#drops most of the data load for speed
    btc.index = [x for x in range(1, len(btc.values)+1)]#indexes df with numbers dont forget to subtract 1
    return btc

def fifty_ma_getter(): #gets current 50 day ma 1row,column1
    fifty_ma = data_cutter().iat[40,6]
    return fifty_ma

def two_ma_getter():#current 200 day moving average
    two_ma = data_cutter().iat[40,7]
    return two_ma
    
def analysis():
    x = fifty_ma_getter()
    y = two_ma_getter()
    if x > y:
        print('true')
    else:
        print('false')


analysis()




