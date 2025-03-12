Initial Approach to project:
1. To get the property tax titles and tables for each url.
2. Automate the process of checking for each state county in a way
that the domain name remains same, just the state and county
names change.
3. Use County_list.csv for getting the links in following form:
https://www.propertyshark.com/mason/info/Property-
Taxes/State/County-county/
Write those links to csv and check if state-counties have
property tax tables if no, return error.
4. As not all state counties have property tax tables separate the
existing links from others, use it for automating the process of
finding the tax tables
Issues faced during the process:
Reading and writing files:
Issue: Reading the writing files is major part of this process and data
was not in a usable format most times as data is pulled in and out of
the code
Solution: required data cleaning to get the right format, data cleaning is very important here.
