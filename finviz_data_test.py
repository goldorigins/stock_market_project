#this portion of the program takes the soup from finviz_data_scrape and sorts it and extracts the table then puts the table in a Pandas dataframe.
import finviz_soup_test
import pandas as pd
import finviz_top
#this top portion of the function picks out the table WITH HTML TAGS ATTACHED
def finviz_tables():
    tableid = finviz_top.user_input()
    soup = finviz_soup_test.finviz()
    sort1 = soup.find('table', attrs={'class':tableid[1]})
    sort2 = sort1.find_all('tr')
#this portion initializes list res and populates the list with the raw table data
    res = []
    for tr in sort2:
        td = tr.find_all('td')
        row = [tr.text.strip() for tr in td if tr.text.strip()]
        if row:
            res.append(row)
#this portion places the raw table data into a pandas data frame.

            
    finviz_table = pd.DataFrame(res, columns=['Ticker','Owner','Relationship','Date','Transaction','Cost','#Shares','Value ($)','Total Co. Shares','SEC Form'])
    
    pd.set_option("display.max.columns", None) #just so it will show all the columns upon print. Still compresses rows.
    
    #finviz_table.index = [x for x in range(1, len(finviz_table.values)+1)] #creates index of rows starting at 1. upon revision you dont need this.
    
    finviz_table1 = finviz_table.drop(0)#this drops the first row that has column labels from the site.
    
    print(finviz_table1)
finviz_tables()






