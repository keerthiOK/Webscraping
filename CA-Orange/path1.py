import re
import csv
from csv import reader,writer
import openpyxl
import pandas as pd
# open file in read mode
"""
data_path="https://www.propertyshark.com/mason/info/Property-Taxes/"

with open('C:/Users/keert/OneDrive/Desktop/County_list.csv', 'r') as read_obj, open('textS','w') as write_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    csv_writer=writer(write_obj)
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        path=data_path+row[0]+"/"+row[1]+"/"
        path = path.replace(' ', '-')
        print(path)
     """   


        #csv_writer.writerow(path)

#stripping the commas

text = open("output.csv", "r")
text = ''.join([i for i in text]) \
    .replace(",", "")
x = open("output2.csv","w")
x.writelines(text)
x.close()