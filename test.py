import btc_data
import doge_data
import bnb_data
import eth_data
import sol1_data
import usdt_data
import ada_data
import xrp_data
import dot1_data
import hex1_data
import usdc_data
import shib_data
import luna1_data
import avax_data
import uni3_data
import link_data
import ltc_data
import matic_data
import algo_data
import bch_data
import vet_data
import axs_data
import xlm_data
import atom1_data
import icp1_data
import pandas as pd
import time
#bring the variables in.
#eache var is a pandas df of yahoo fincance data
while True:
    
    time.sleep(1)
    bnb = bnb_data.bnb_ma()
    btc = btc_data.btc_ma()
    doge = doge_data.doge_ma()
    eth = eth_data.eth_ma()
    sol1 = sol1_data.sol1_ma()
    usdt = usdt_data.usdt_ma()
    ada = ada_data.ada_ma()
    xrp = xrp_data.xrp_ma()
    dot1 = dot1_data.dot1_ma()
    hex1 = hex1_data.hex1_ma()
    usdc = usdc_data.usdc_ma()
    shib = shib_data.shib_ma()
    luna1 = luna1_data.luna1_ma()
    avax = avax_data.avax_ma()
    uni3 = uni3_data.uni3_ma()
    link = link_data.link_ma()
    ltc = ltc_data.ltc_ma()
    matic = matic_data.matic_ma()
    algo = algo_data.algo_ma()
    bch = bch_data.bch_ma()
    vet = vet_data.vet_ma()
    axs = axs_data.axs_ma()
    xlm = xlm_data.xlm_ma()
    atom1 = atom1_data.atom1_ma()
    icp1 = icp1_data.icp1_ma()
    
    
#dont forget to add your ticker to the list
    ticker_list = [bnb,btc,doge,eth,sol1,usdt,ada,xrp,dot1,hex1,usdc,shib,luna1,avax,uni3,link,ltc,matic,algo,bch,vet,axs,xlm,atom1,icp1]
    ticker_list_txt = ['bnb','btc','doge','eth','sol1','usdt','ada','xrp','dot1','hex','usdc','shib','luna1','avax','uni3','link','ltc','matic','algo','bch','vet','axs','xlm','atom1','icp1']


    for ticker in range(len(ticker_list)): #takes all tickers and puts them to list
        current_ticker = ticker_list[ticker]


        current_ticker.drop(current_ticker.index[1:8700], inplace = True)#drops most of the data load for speed
        current_ticker.index = [x for x in range(1, len(current_ticker.values)+1)]#indexes df with numbers dont forget to subtract 1


        def fifty_ma_getter(): #gets current 50 day ma 1row,column1
            fifty_ma = current_ticker.iat[0,0]
            return fifty_ma

        def two_ma_getter():#current 200 day moving average
            two_ma = current_ticker.iat[0,0]
            return two_ma
    
        def analysis():
            x = fifty_ma_getter()
            y = two_ma_getter()
            fifty_list = []
            two_list = []
            if x > y:# tells if 50ma is greater than 200ma
                fifty_list.append('50T' + ticker_list_txt[ticker])
            
            else:
                fifty_list.append('50F' + ticker_list_txt[ticker])
            
            if x < y:# tells if 200ma is greater than 50ma
                two_list.append('200T' + ticker_list_txt[ticker])
            
            else:
                two_list.append('200F' + ticker_list_txt[ticker])
            print(two_list, fifty_list)


    analysis()
