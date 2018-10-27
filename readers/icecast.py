import streamcables


def scraper(soup):
    txt = soup.select("td.streamstats")[-1].text
    txt = " ".join(txt.split())

    return txt.split(" - ")


def register():
    streamcables.logging.info("icecast reader registered.")
    return scraper
