#this program is the top of the Finviz project.
#it goes out to finviz insider and scrapes the site using cloudscraper to circimvent the Cloudfare security
#then it uses BS4 to generate a BS$ object which is passed out for sorting in NoShares_data
import cloudscraper
import lxml
from bs4 import BeautifulSoup
import finviz_top

def main():
    finviz()

def finviz():
#target site URL (currently list)
    user_input = finviz_top.user_input()
# returns a CloudScraper instance
    scraper = cloudscraper.create_scraper()
#scrapes entire page on url
    finviz_scrape = scraper.get(user_input[0])
    soup1 = BeautifulSoup(finviz_scrape.text,features="lxml")
    print(soup1)
    return soup1

main()


