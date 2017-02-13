# python3
import datetime
import random
import re
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

random.seed(datetime.datetime.now())

def get_links(article_url):
    html = urlopen('http://en.wikipedia.org' + article_url)
    bsObj = bs(html)
    return  bsObj.find('div', { 'id': 'bodyContent' })\
                 .findAll('a', href = re.compile('^(/wiki/)((?!:).)*$')):

links = get_links('/wiki/Kevin_Bacon')

while len(links) > 0:
    new_article = links[random.randint(0, len(links) - 1)].attrs['href']
    print(new_article)
    links = get_links(new_article)
                        
