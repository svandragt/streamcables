#!/usr/bin/env python3.7
from bs4 import BeautifulSoup
import importlib
import logging
import requests
import sys
import toml


def register_reader(reader):
    global ins
    ins = {**ins, **reader}


def url_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


def main():
    setup_logging()

    settings = toml.load("settings.toml")
    reader_name = settings["main"]["reader"]

    soup = url_soup(settings[reader_name]["url"])

    reader = plugins(["readers." + reader_name + ".register"])[0]
    artist, title = reader(soup)

    print(artist, ":::", title)


def plugins(fetch_handlers):
    if not fetch_handlers:
        fetch_handlers = FETCH_HANDLERS
    plugin_list = []
    for handler_name in fetch_handlers:
        package, classname = handler_name.rsplit(".", 1)
        try:
            handler_class = getattr(importlib.import_module(package), classname)
            plugin_list.append(handler_class())
        except NotImplementedError:
            # Skip missing plugins so that they can be ommitted from
            # installation if desired
            log("FetchHandler {} not found, skipping plugin".format(handler_name))
    return plugin_list


def setup_logging():
    """Configure console logging. Info and below go to stdout, others go to stderr.

    :param int verbose: Verbosity level. > 0 print debug statements. > 1 passed to sphinx-build.
    :param bool colors: Print color text in non-verbose mode.
    :param str name: Which logger name to set handlers to. Used for testing.
    """
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    handler_stdout = logging.StreamHandler(sys.stdout)
    handler_stdout.setLevel(logging.DEBUG)
    handler_stdout.addFilter(
        type(
            "",
            (logging.Filter,),
            {"filter": staticmethod(lambda r: r.levelno <= logging.INFO)},
        )
    )
    root_logger.addHandler(handler_stdout)

    handler_stderr = logging.StreamHandler(sys.stderr)
    handler_stderr.setLevel(logging.WARNING)
    root_logger.addHandler(handler_stderr)


if __name__ == "__main__":
    main()
