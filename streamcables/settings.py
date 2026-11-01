# settings.py

import logging
import os
import sys
from shutil import copyfile

import toml
from appdirs import AppDirs

config = {}


def init():
    global config
    config = {"dirs": AppDirs("StreamCables", "NoNoTools")}

    config["settings_fn"] = config["dirs"].user_data_dir + "/settings.toml"
    try:
        config = {**config, **toml.load(config["settings_fn"])}
        print("Reading " + config["settings_fn"] + "...")
    except FileNotFoundError:
        logging.warning("Edit " + config["settings_fn"] + "!")
        src = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "settings.default.toml"
        )
        os.makedirs(config["dirs"].user_data_dir, exist_ok=True)
        copyfile(src, config["settings_fn"])
        sys.exit(1)
