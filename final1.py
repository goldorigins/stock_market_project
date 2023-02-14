#The purpose of this program is to scrape data from the internet.
#the scraped data should be market data
#with the market data the program will have an algorythm
#the algorythm will output desireable market buys
#these market buys will be to begin with iron flys or their inverses
#to begin with the flys should have at max a risk of 50% of the max profit
#the outputs should be scans of many tickers for a wide variety of options
############################################################################
############################################################################
############################################################################
############################################################################
import bs4
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
#sets desired ticker. in the future you could make this long
def ticker():
    ticker = ['GME','MFA','NYMT','AMC']
    return ticker
#creates list of urls for scrapet to grab
def ticker_site():
    ticker_site = ['https://finance.yahoo.com/quote/'+x+'/options?p='+x for x in ticker()]
    return ticker_site
#runs a get on all the links genered by the ticker list in ticker()
def ticker_gets():
    for i in range(len(ticker_site())):
        option_page = ticker_site()
        requested_page = requests.get(option_page[i])
        return requested_page
#hopefully this will make soup out of the gets
def soup_maker():
    for i in range(len(ticker_site())):
        soup = ticker_gets()
        gotten_list = soup
        ticker_soup = BeautifulSoup(gotten_list.text,'html.parser')
        return ticker_soup

def table_make():
    ticker = soup_maker()
    option_table = ticker.find('table')
    option_rows = option_table.find_all('tr')
    for tr in option_rows:
        option_row_data = tr.find_all('td')
        row = [i.text for i in option_row_data]
        print(row)
print(table_make())

#currently, i am trying to make soup out of the gets. I need it to do it for all the tickers independently
#and put the soup into another list that can be ran through by soup.find to get table id's for a later
#soup.find because the table ids are different on every page so i need a variable for option_table = option_soup.find('table',attrs={'data-reactid' : table_id}. 
                   





