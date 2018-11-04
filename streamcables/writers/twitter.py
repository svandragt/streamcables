import streamcables
import tweepy
import os
import sys
import subprocess

auth = {}
tokens_fn = "twitter.toml"


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


def publish(info):
    global auth, tokens_fn
    api = tweepy.API(auth)

    try:
        Status = api.update_status(
            " is #NowPlaying ♫: " + info["now"] + " #streamcables"
        )
    except tweepy.TweepError:
        os.remove(tokens_fn)
        setup_auth()

    public_tweets = api.home_timeline()

    for tweet in public_tweets[0:1]:
        print(tweet.text)


def register():
    setup_auth()

    streamcables.logging.info("[twitter] writer registered.")
    return publish


def setup_auth():
    global auth, tokens_fn

    settings = streamcables.settings

    app_key = settings["twitter"]["consumer-key"]
    app_secret = settings["twitter"]["consumer-secret"]

    auth = tweepy.OAuthHandler(app_key, app_secret)

    try:
        tokens = streamcables.toml.load(tokens_fn)
    except (FileNotFoundError,KeyError) as e:
        # new authorization request
        streamcables.logging.info("[twitter] new access token required")
        tokens = setup_auth_tokens()

    auth.set_access_token(tokens["access_token"], tokens["access_token_secret"])
    streamcables.logging.info("[twitter] reused access token.")


def setup_auth_tokens():
    global auth, tokens_fn
    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError:
        print("Error! Failed to get request token.")

    open_url(redirect_url)
    verifier_code = input("Verifier code: ")
    auth.get_access_token(verifier_code)

    tokens = {
        "access_token": auth.access_token,
        "access_token_secret": auth.access_token_secret,
    }
    
    with open(tokens_fn, "w") as f:
        toml_string = streamcables.toml.dumps(tokens)
        f.write(toml_string)
    
    return tokens

