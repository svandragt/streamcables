#!/usr/bin/env python3.7
from bs4 import BeautifulSoup
import requests


def url_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


def icecast_reader(soup):

    txt = soup.select("td.streamstats")[-1].text
    txt = " ".join(txt.split())

    return txt.split(" - ")


soup = url_soup("http://listen.snowcloudfm.com:8000/status.xsl")
artist, title = icecast_reader(soup)
print(artist, title)

