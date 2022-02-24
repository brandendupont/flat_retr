import sys
import pandas as pd
import numpy as np
import requests as r
from bs4 import BeautifulSoup

## Global Vars
#url path for RETR Data
RETR_DATA_PAGE = 'https://www.revenue.wi.gov/pages/eretr/data-home.aspx'


def get_retr_links(url_page):
    
    """
    Get all links in a web page
    """
        
    res = r.get(url_page)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    return [link.get('href') for link in soup.find_all('a')]

def filter_url(txt):
    return ".zip" in str(txt)

def get_subset_mke_retr(retr_zip_url):
    
    """
    Get all retr files from DOR website and return Milwaukee RETR data.
    """
    
    # all files
    retr_zip_url_df = []
    
    for monthly_retr_url in retr_zip_url:
        
        #read data
        retr_zip = pd.read_csv(monthly_retr_url, compression='zip', header=0, sep=',', quotechar='"', encoding = "ISO-8859-1")
        
        #subset
        retr_zip = retr_zip[retr_zip['CountyName'].str.lower().str.contains('milw') == True]
        
        # append
        retr_zip_url_df.append(retr_zip)
        
    
    return retr_zip_url_df


if __name__ == "__main__":

    print("argv :", sys.argv)

    # get all links at retr page
    urls = get_retr_links(url_page=RETR_DATA_PAGE)
    # filter list to only include zip files
    filtered_url = list(filter(filter_url,urls))

    # generate urls from wi revenue
    retr_zip_url = ["https://www.revenue.wi.gov" + i for i in filtered_url]

    # get zipped data, filter to include only milwaukee county, 
    mke_retr_mn = get_subset_mke_retr(retr_zip_url=retr_zip_url)

    # make sure the .zip url size is the same as the list of dataframes
    assert len(mke_retr_mn) == len(retr_zip_url)

    #combine dataframes
    mke_retr = pd.concat(mke_retr_mn)

    #save data
    mke_retr.to_csv('flat_mke_retr.csv', index=False)

    df = pd.DataFrame(np.random.randint(0, 100,\
         size=(10, 4)), columns=list('ABCD'))

    df.to_csv("df_output.csv")
