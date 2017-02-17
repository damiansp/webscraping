#!usr/bin/env python3

import re
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

pages = set()

def get_links(page_url):
    global pages
    html = urlopen('http://en.wikipedia.org' + page_url)
    bs_obj = bs(html, 'html.parser')

    try:
        print(bs_obj.h1.get_text())
        print(bs_obj.find(id = 'mw-content-text').findAll('p')[0])
        print(bs_obj.find(id = 'ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('Something missing on this page, but no fear... Sally forth!')

    for link in bs_obj.findAll('a', href = re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # New page found
                new_page = link.attrs['href']
                print('-----------------\n' + new_page)

                pages.add(new_page)
                get_links(new_page)

get_links('')
