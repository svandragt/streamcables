import streamcables


def scraper():
    settings = streamcables.settings["icecast"]
    soup = url_soup(settings["url"])

    trs = soup.select("table.yellowkeys")[0].select("tr")
    info = {}
    for tr in trs:
        k, v = tr.contents
        info[k.text] = " ".join(v.text.split())

    info["now"] = info["Currently playing:"]
    info["hash"] = hash(info["now"])

    return info


def register():
    streamcables.logging.info("[icecast] reader registered.")
    return scraper


def url_soup(url):
    r = streamcables.requests.get(url)
    soup = streamcables.BeautifulSoup(r.text, "html.parser")
    return soup
