from streamcables import logging, maya


def printer(args):
    m = maya.now().local_datetime()
    print("")
    print(m)
    if args["artist"]:
        print("Artist:", args["artist"])
    if args["title"]:
        print("Title:", args["title"])


def register():
    logging.info("stdout writer registered.")
    return printer
