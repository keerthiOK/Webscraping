import bs4
import requests
try:
    url=['https://www.propertyshark.com/mason/info/Property-Taxes/AL/Bibb-County/',
    'https://www.propertyshark.com/mason/info/Property-Taxes/TX/Harris-County/',
            'https://www.propertyshark.com/mason/info/Property-Taxes/OK/Tulsa-County/',
 'https://www.propertyshark.com/mason/info/Property-Taxes/AL/Bibb-County/',
        'https://www.propertyshark.com/mason/info/Property-Taxes/WI/Wood-County/']
    for u in url:
        site=requests.get(u)
        site.raise_for_status()
        soup=bs4.BeautifulSoup(site.text,'lxml')
        gdp = soup.find_all("h1", attrs={"class": "lp t"})
        print(gdp[0].text)
        p=[]
        if gdp[0]!='raised index error':
            p.append(u)
            print(p)
            continue
        
        
except IndexError:
    print('raised index error')
   
    
    
    
    
else:
    print('success')
     