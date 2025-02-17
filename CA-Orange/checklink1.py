import bs4
import requests
import csv
import pandas as pd
url=['https://www.propertyshark.com/mason/info/Property-Taxes/AL/Bibb-County/',
    'https://www.propertyshark.com/mason/info/Property-Taxes/TX/Harris-County/',
            'https://www.propertyshark.com/mason/info/Property-Taxes/OK/Tulsa-County/',
 'https://www.propertyshark.com/mason/info/Property-Taxes/AL/Bibb-County/',
        'https://www.propertyshark.com/mason/info/Property-Taxes/WI/Wood-County/',
        'https://www.propertyshark.com/mason/info/Property-Taxes/CA/Orange-County/'
        ]

    
for u in url:
    try:
        site=requests.get(u)
        site.raise_for_status()
        soup=bs4.BeautifulSoup(site.text,'lxml')
        #gdp = soup.find_all("h1", attrs={"class": "lp t"})
        #print(gdp[0].text)
        first_h1 = soup.select('h1')[0].text
        
        #print(first_h1)
        p=[]
        if first_h1!='raised error':
            p.append(u)
        print(p)
        df = pd.DataFrame(p)
        col=df.columns
        #df=df.set_index(col[0])
        print(df)
        for r in p:
           with open("L.csv", "a") as file_object:
               file_object.write('\n'+r)
        
            
    except IndexError:
        print('raised error')
        
        continue


    
    
    
    
#df.to_csv('workinglinks.csv', index=False)
