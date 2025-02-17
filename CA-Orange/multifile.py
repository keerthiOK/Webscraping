from bs4 import BeautifulSoup
import requests
import bs4
import re
import csv
from csv import reader,writer
import openpyxl
import pandas as pd
import sys
with open('output2.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    """
    text = open("Original.csv", "r")
    text = ''.join([i for i in text]) \
    .replace(",", "")
    """
    csv_reader = reader(read_obj)
    rows=[]
    for row in csv_reader:
          text = ''.join([i for i in row]) \
    .replace("[]", "")
          rows.append(text)
          res=[]
          for ele in rows:
              if ele.strip():
                  res.append(ele)
    for u in res:
              try:
                site=requests.get(u)
                site.raise_for_status()
                soup=bs4.BeautifulSoup(site.text,'lxml')
                first_h1 = soup.select('h1')[0].text
                #print(first_h1)
                p=[]
                if first_h1!='raised error':
                   p.append(u)
                    #print(p)
                  #df = pd.DataFrame(p)
                  #col=df.columns
                  #df=df.set_index(col[0])
                  #print(df)
                  #df.to_excel('Chech.xlsx', index=False)
                
                   for r in p:
                       with open("L3.csv", "a") as file_object:
                          file_object.write('\n'+r)
                       #x = open("L2.csv","a")
                       #x.writelines('\n'+r)
                       #x.close()
        
            
              except IndexError:
                          print('raised error')
                          continue
              except Exception as inst:
                  print (inst)

    
    

          

  

"""
for url in site:
        response = requests.get(url)
        soup = BeautifulSoup(url, "lxml")    
        first_h1 = soup.select('h1')[0].text
        gdp = soup.find_all("table", attrs={"class": "narrow90 sum-table"})
        table1 = gdp[0]
        print(table1)

"""
"""
text = open("output2.csv", "r")
text = ''.join([i for i in text]) \
    .replace("[]", "")
x = open("output4.csv","w")
x.writelines(text)
x.close()
"""