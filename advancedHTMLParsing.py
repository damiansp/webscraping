# python3
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bsObj = bs(html)
nameList = bsObj.findAll('span', { 'class': 'green' })

for name in nameList:
    print(name.get_text())
