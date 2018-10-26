#!/usr/bin/env python3.7
from bs4 import BeautifulSoup
import requests
import toml


def register_reader(reader):
    global ins
    ins = {**ins, **reader}


def url_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


def main():
    global ins

    from readers import icecast

    register_reader({"icecast": icecast.icecast_reader})

    settings = toml.load("settings.toml")

    soup = url_soup("http://listen.snowcloudfm.com:8000/status.xsl")
    artist, title = ins[settings["reader"]](soup)
    print(artist, title)


if __name__ == "__main__":
    ins = {}
    main()
    print(ins)
