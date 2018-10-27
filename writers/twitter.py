import streamcables
import tweepy
import os
import sys
import subprocess

auth = {}


def open_url(url):
    if sys.platform == "win32":
        os.startfile(url)
    elif sys.platform == "darwin":
        subprocess.Popen(["open", url])
    else:
        try:
            subprocess.Popen(["xdg-open", url])
        except OSError:
            print("Please open a browser on: " + url)


def publish(args):
    global auth
    api = tweepy.API(auth)

    public_tweets = api.home_timeline()

    for tweet in public_tweets[0:1]:
        print(tweet.text)


def register():

    settings = streamcables.settings
    setup_auth(settings)

    streamcables.logging.info("[twitter] writer registered.")
    return publish


def setup_auth(settings):
    global auth

    app_key = settings["twitter"]["app-key"]
    app_secret = settings["twitter"]["app-secret"]

    auth = tweepy.OAuthHandler(app_key, app_secret)

    tokens_fn = "twitter.toml"
    try:
        tokens = streamcables.toml.load(tokens_fn)
        auth.set_access_token(tokens["access_token"], tokens["access_token_secret"])
        streamcables.logging.info("[twitter] reused access token.")
    except FileNotFoundError or KeyError:
        # new authorization request
        tokens = {}
        streamcables.logging.info("[twitter] new access token required")
        auth = setup_auth_new(auth)


def setup_auth_new(auth):
    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError:
        print("Error! Failed to get request token.")

    open_url(redirect_url)
    verifier_code = input("Verifier code: ")
    auth.get_access_token(verifier_code)

    with open(tokens_fn, "w") as f:
        toml_string = streamcables.toml.dumps(
            {
                "access_token": auth.access_token,
                "access_token_secret": auth.access_token_secret,
            }
        )
        f.write(toml_string)

