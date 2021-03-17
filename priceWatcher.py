# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 23:30:38 2021

@author: kgran
"""
#Followed example from towards data science article Scraping Amazon Stores to Generate Price Alerts (https://towardsdatascience.com/scraping-multiple-amazon-stores-with-python-5eab811453a8)

#Imported Packages
import requests
from glob import glob
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from time import sleep

# http://www.networkinghowtos.com/howto/common-user-agent-list/
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
    
# imports a csv file with the url's to scrape
prod_tracker = pd.read_csv('products/Products_To_Track.csv', sep=',')
prod_tracker_URLS = prod_tracker.url

# fetch the url
page = requests.get(prod_tracker_URLS[0], headers=HEADERS)

# create the object that will contain all the info in the url
soup = BeautifulSoup(page.content, features="lxml")