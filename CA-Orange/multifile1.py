from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import openpyxl
from pandas.io.formats.style import Styler

# Site URL
url_list=['https://www.propertyshark.com/mason/info/Property-Taxes/OK/Tulsa-County/',
'https://www.propertyshark.com/mason/info/Property-Taxes/OH/Wood-County/',
'https://www.propertyshark.com/mason/info/Property-Taxes/TX/Harris-County/']

url="https://www.propertyshark.com/mason/info/Property-Taxes/TX/harris-County/"
for urls in url:
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    gdp = soup.find_all("table", attrs={"class": "narrow90 sum-table"})
    first_h1 = soup.select('h1')[0].text
    print(first_h1)
    table1 = gdp[0]
    body = table1.find_all("tr")
    head = body[0] 
    body_rows = body[1:] 
    headings = []
    for item in head.find_all("th"):
        item = (item.text).rstrip("\n")
        headings.append(item)

    all_rows = [] 
    for row_num in range(len(body_rows)): 
       row = [] 
       for row_item in body_rows[row_num].find_all("td"): 
        
           aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
           row.append(aa)
    all_rows.append(row)
    
df = pd.DataFrame(data=all_rows,columns=headings)
col=df.columns
df=df.set_index(col[0])
print(df)


