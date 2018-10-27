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


def printer(args):
    global auth
    api = tweepy.API(auth)

    public_tweets = api.home_timeline()

    for tweet in public_tweets[0:1]:
        print(tweet.text)


def register():
    global auth

    settings = streamcables.settings

    app_key = settings["twitter"]["app-key"]
    app_secret = settings["twitter"]["app-secret"]
    tokens_fn = 'twitter.toml'

    auth = tweepy.OAuthHandler(app_key, app_secret)

    try:
        tokens = streamcables.toml.load(tokens_fn);
    except FileNotFoundError:
        tokens = {}

    try:
        auth.set_access_token(tokens['access_token'], tokens['access_token_secret'])
    except KeyError:
        try:
            redirect_url = auth.get_authorization_url()
        except tweepy.TweepError:
            print("Error! Failed to get request token.")

        open_url(redirect_url)
        verifier_code = input("Verifier code: ")
        auth.get_access_token(verifier_code)

        tokens = {
            'access_token': auth.access_token, 
            'access_token_secret': auth.access_token_secret,
        }

        with open(tokens_fn, 'w') as f:
            toml_string = streamcables.toml.dumps(tokens)
            f.write(toml_string)

    streamcables.logging.info("twitter writer registered.")
    return printer
