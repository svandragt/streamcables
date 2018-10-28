from streamcables import logging, maya


def publish(info):
    m = maya.now().local_datetime()
    print("")
    print(m)
    print("Now playing:", info)


def register():
    logging.info("[stdout] writer registered.")
    return publish
