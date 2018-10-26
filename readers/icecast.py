import streamcables


def icecast_reader(soup):

    txt = soup.select("td.streamstats")[-1].text
    txt = " ".join(txt.split())

    return txt.split(" - ")
