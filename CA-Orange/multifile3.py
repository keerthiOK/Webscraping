from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
from csv import reader, writer
import bs4
import sys
import csv
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
"""
url_list=['https://www.propertyshark.com/mason/info/Property-Taxes/OK/Tulsa-County/',
'https://www.propertyshark.com/mason/info/Property-Taxes/OH/Wood-County/',
'https://www.propertyshark.com/mason/info/Property-Taxes/TX/Harris-County/']
"""
"""
url_list=[
'https://www.propertyshark.com/mason/info/Property-Taxes/TX/Harris-County/']
"""
with open('L3.csv', 'r') as read_obj:
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
                gdp = soup.find_all("table", attrs={"class": "narrow90 sum-table"})
                first_h1 = soup.select('h1')[0].text
                #print(first_h1)
                #print("Number of tables on site: ",len(gdp))
                table1 = gdp[0]

                body = table1.find_all("tr")
                # Head values (Column names) are the first items of the body list
                head = body[0] # 0th item is the header row
                body_rows = body[1:] # All other items becomes the rest of the rows

                # Lets now iterate through the head HTML code and make list of clean headings

                # Declare empty list to keep Columns names
                headings = []
                for item in head.find_all("th"): # loop through all th elements
    # convert the th elements to text and strip "\n"
                    item = (item.text).rstrip("\n")
    # append the clean column name to headings
                    headings.append(item)
                #print(headings)
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
                        #print(aa)
        #append aa to row - note one row entry is being appended
                        row.append(aa)
    # append one row to all_rows
                    all_rows.append(row)
                #print(all_rows)
                with open("Finalfile1.csv", "a") as file_object:
                    file_object.write('\n '+first_h1+'\n')
                    file_object.write('\n')


                with open('Finalfile1.csv', 'a', newline='') as f:
                     writer = csv.writer(f)
                     writer.writerow(headings)
                     writer.writerows(all_rows)
                

                df = pd.DataFrame(data=all_rows,columns=headings)
                col=df.columns
                df=df.set_index(col[0])
                #df.to_excel('cg.xlsx',index=False)    
                

                    #df.to_csv('Final_Exec_Test.csv', index=True)
                #with open("Final_Exec_Test.csv", "a") as file_object:
                #   file_object.writerow(all_rows)
                
                    #print(df)
                    #df.to_csv('ppp.csv')

                     #     with open("Final_Exec_Test.csv", "a") as file_object:
                      #         file_object.write(p)                          


                    #df.to_csv('Final_Exec_Test.csv', index=True)
                #with open("Final_Exec_Test.csv", "a") as file_object:
                #   file_object.writerow(all_rows)
                       
        except IndexError:
                          print('raised error')
                          continue
                

   

         
