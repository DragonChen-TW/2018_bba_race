import requests
from bs4 import BeautifulSoup

def get_source(url):
    return requests.get(url)

def get_soup(url):
    html = get_source(url).text
    return BeautifulSoup(html, 'html.parser')
