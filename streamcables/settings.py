# settings.py

import toml
from appdirs import AppDirs

config = {}


def init():
    global config
    config = {'dirs': AppDirs("StreamCables", "NoNoTools")}

    config['settings_fn'] = config['dirs'].user_data_dir + "/settings.toml"
    try:
        config = {**config, **toml.load(config['settings_fn'])}
    except FileNotFoundError:
        print("Missing " + config['settings_fn'])
        exit(1)
