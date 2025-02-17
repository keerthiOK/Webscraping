from bs4 import BeautifulSoup
import requests
import re
import csv
from csv import reader,writer
import openpyxl
import pandas as pd
with open('L.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    
    csv_reader = reader(read_obj)
    rows=[]
    for row in csv_reader:
        #print(row)
        
        #print(row)
        text = ''.join([i for i in row]) \
    .replace("[]", "")
        #print(text)
        rows.append(text)
    print(rows)
"""
site=requests.get(rows)  
site.raise_for_status()    


for url in site:
        response = requests.get(url)
        soup = BeautifulSoup(url, "lxml")    
        first_h1 = soup.select('h1')[0].text
        gdp = soup.find_all("table", attrs={"class": "narrow90 sum-table"})
        table1 = gdp[0]
        print(table1)

"""
"""
text = open("L.csv", "r")
text = ''.join([i for i in text]) \
    .replace("[]", "")

x = open("output4.csv","w")
x.writelines(text)
x.close()
"""