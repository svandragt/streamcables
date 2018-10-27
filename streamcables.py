#!/usr/bin/env python3.6
from bs4 import BeautifulSoup
import argparse
import importlib
import logging
import maya
import requests
import sys
import time
import toml


settings = toml.load("settings.toml")


def arg_parse():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--debug",
        help="Print lots of debugging statements",
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
        default=logging.WARNING,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="Be verbose",
        action="store_const",
        dest="loglevel",
        const=logging.INFO,
    )
    args = parser.parse_args()
    return args


def main():
    global settings
    args = arg_parse()
    setup_logging(args.loglevel)

    print("StreamCables 0.1")

    reader_name = settings["main"]["reader"]
    writer_names = settings["main"]["writers"]
    refresh_rate = settings["main"]["refresh-rate"]

    rs = ["readers." + reader_name + ".register"]
    reader = plugins(rs)[0]

    ws = []
    for name in writer_names:
        ws.append("writers." + name + ".register")
    writers = plugins(ws)

    logging.info("-------START----------")
    last_artist = last_title = ""
    try:
        while True:
            soup = url_soup(settings[reader_name]["url"])
            args = reader(soup)
            artist = args[-2]
            title = args[-1]

            if last_artist != artist or last_title != title:
                for writer in writers:
                    writer({"artist": artist, "title": title})
                last_artist, last_title = artist, title

            for i in range(refresh_rate * 2):
                print("/-\|"[i % 4], end="\b", flush=True)
                time.sleep(0.5)
    except KeyboardInterrupt:
        print("")
        pass

    print("Bye!")


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


def setup_logging(loglevel):
    """Configure console logging. Info and below go to stdout, others go to stderr.

    :param int verbose: Verbosity level. > 0 print debug statements. > 1 passed to sphinx-build.
    :param bool colors: Print color text in non-verbose mode.
    :param str name: Which logger name to set handlers to. Used for testing.
    """
    root_logger = logging.getLogger()
    root_logger.setLevel(loglevel)

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


def url_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


if __name__ == "__main__":
    main()
