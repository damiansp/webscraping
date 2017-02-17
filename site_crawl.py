#!/usr/bin/env python3

import re
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

pages = set()

def get_links(page_url):
    global pages
    html = urlopen('http://en.wikipedia.org' + page_url)
    bs_obj = bs(html, 'html.parser')

    for link in bs_obj.findAll('a', href = re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # New page found
                new_page = link.attrs['href']
                print(new_page)
                pages.add(new_page)
                get_links(new_page)

get_links('')
