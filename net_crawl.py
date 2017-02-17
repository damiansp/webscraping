#!/usr/bin/env python3

import datetime
import random
import re
import ssl
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse
from urllib.request import urlopen

pages = set()
context = ssl._create_unverified_context()
random.seed(datetime.datetime.now())

# Retrieves a list of all internal links found on a page
def get_internal_links(bs_obj, include_url):
    include_url = (urlparse(include_url).scheme +
                   '://' +
                   urlparse(include_url).netloc)
    internal_links = []

    # Find all links beginning with '/'
    for link in bs_obj.findaAll(
            'a', href = re.compile('^(/|.*' + include_url + ')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internal_links:
                if link.attrs['href'].startswith('/'):
                    internal_links.append(include_url + link.attrs['href'])
                else:
                    internal_links.append(link.attrs['href'])

    return internal_links

# Retrieve a list of external links found on page
def get_external_links(bs_obj, exclude_url):
    external_links = []

    # Finds links starting with 'http' not containing the current url
    for link in bs_obj.findAll(
        'a', href = re.compile('^(http|www)((?!' + exclude_url + ').)*$')):

        if link.attrs['href'] is not None:
            if  link.attrs['href'] not in external_links:
                external_links.append(link.attrs['href'])

    return external_links

def get_random_external_link(starting_page):
    html = urlopen(starting_page, context = context)
    bs_obj = bs(html, 'html.parser')
    external_links = get_external_links(bs_obj, urlparse(starting_page).netloc)

    if len(external_links) == 0:
        print('No external links, looking in the site for one...')
        domain = (urlparse(starting_page).scheme +
                  '://' +
                  urlparse(starting_page).netloc)
        internal_links = get_internal_links(bs_obj, domain)

        return get_random_external_link(
            internal_links[random.randint(0, len(internal_links) - 1)])
    else:
        return external_links[random.randint(0, len(external_links) - 1)]

def follow_external_only(starting_site):
    external_link = get_random_external_link(starting_site)
    print('Following random external link:' + external_link)

    follow_external_only(external_link)

follow_external_only('http://oreilly.com')

                              
            
