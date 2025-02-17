"""from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import requests
import urllib
"""
"""
html_page = urllib.request.urlopen("https://abc.com")
soup = BeautifulSoup(html_page,'lxml')
for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    print (link.get('href'))

url_list = ['https://nocable.org/browse-stations/callsign/cadenatres-linares-nl',
            'https://nocable.org/browse-stations/callsign/k27hm-d-quanah-tx']
data = []
for url in url_list:
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "lxml")
    gdp = soup.find_all("h1", attrs={"class": "dashboard__heading--primary"})
    #print(gdp[0].text)
    data.append(gdp[0].text)
    print(data)
"""
"""
url_list='https://www.propertyshark.com/mason/info/Property-Taxes/OH/Wood-County/'
data = []
html_content = requests.get(url_list).text

#page = urllib.request.urlopen(url_list)
soup = BeautifulSoup(html_content, "lxml")
gdp = soup.find_all("h1", attrs={"class": "lp t"})
#print(gdp[0].text)
data.append(gdp[0].text)
print(data)"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
#import openpyxl
#from pandas.io.formats.style import Styler
"""
# Site URL
url=['https://www.propertyshark.com/mason/info/Property-Taxes/OK/tulsa-County/',
'https://www.propertyshark.com/mason/info/Property-Taxes/OH/Wood-County/']

html_content = requests.get(url).text

# Parse HTML code for the entire site
soup = BeautifulSoup(html_content, "lxml")
#gdp = soup.find_all("table", attrs={"class": "narrow90 sum-table"})
# Extract first <h1>(...)</h1> text
first_h1 = soup.select('h1')[0].text
print(first_h1)
"""

url_list=['https://www.propertyshark.com/mason/info/Property-Taxes/OK/Tulsa-County/',
'https://www.propertyshark.com/mason/info/Property-Taxes/OH/Wood-County/',
'https://www.propertyshark.com/mason/info/Property-Taxes/TX/Harris-County/']
"""

url_list=[
'https://www.propertyshark.com/mason/info/Property-Taxes/TX/Harris-County/']
"""
data = []
for url in url_list:
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")
    #gdp = soup.find_all("h1", attrs={"class": "lp t"})
    #print(gdp[0].text)
    gdp = soup.find_all("table", attrs={"class": "narrow90 sum-table"})
    first_h1 = soup.select('h1')[0].text
    print(first_h1)
    table1 = gdp[0]
    #print(table1)
    body = table1.find_all("tr")
    #print(body)
    head = body[0] # 0th item is the header row
    #print(head)
    body_rows = body[1:] # All other items becomes the rest of the rows
    #print(body_rows)
# Lets now iterate through the head HTML code and make list of clean headings

# Declare empty list to keep Columns names
    headings = []
    for item in head.find_all("th"): # loop through all th elements
    # convert the th elements to text and strip "\n"
        item = (item.text).rstrip("\n")
    # append the clean column name to headings
        headings.append(item)
    #print(headings)
# Next is now to loop though the rest of the rows

#print(body_rows[0])
    all_rows = [] # will be a list for list for all rows
    for row_num in range(len(body_rows)): # A row at a time
        row = [] # this will old entries for one row
        for row_item in body_rows[row_num].find_all("td"): #loop through all row entries
        # row_item.text removes the tags from the entries
        # the following regex is to remove \xa0 and \n and comma from row_item.text
        # xa0 encodes the flag, \n is the newline and comma separates thousands in numbers
           aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
        #append aa to row - note one row entry is being appended
           row.append(aa)
    # append one row to all_rows
    all_rows.append(row)
    #print(all_rows)
    df = pd.DataFrame(data=all_rows,columns=headings)
    col=df.columns
    df=df.set_index(col[0])
    print(df)
df.to_csv('datatest.csv', index=True)

#df.to_excel("data.xlsx", index=True)

#df = pd.DataFrame(list())
#df.to_csv('data2.csv')
#with open("Data2.csv", "a") as file_object:
#   file_object.write('\n '+first_h1)



   


    

    #print(data)