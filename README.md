# Introduction

StreamCables connects to audio streams and sends the metadata to other places. It's built mainly to connect to Icecast and Shoutcast streams, and to post track lists to social media. It can read from and write to multiple services, and it's written for extensibility.

Currently it supports these readers:

  - Icecast

Currently it supports these writers:

  - stdout (the screen)
  - Twitter

Feel free to submit a pull request if your workflow is missing.

# Setup

StreamCables requires Python 3.11+ and [uv](https://docs.astral.sh/uv/).
Install it as follows:

```
git clone <repository url> streamcables
cd streamcables
uv sync
```

Run the program as follows:

```
uv run python streamcables/streamcables.py
# shorter version
make run
```

# Settings and configuration

On first run, StreamCables asks you to create a settings file, and prints the expected location to the screen. This settings file must contain one reader and one or more writers. To use the Twitter functionality, you need a registered Twitter developer account and application, which gives you the key and secret.

Example settings.toml:

```
[main]
reader = 'icecast'
writers = ['stdout', 'twitter']
refresh-rate = 20

[icecast]
url="http://localhost:8000/status.xsl"

[twitter]
consumer-key="Your twitter app consumer key"
consumer-secret="Your twitter app consumer secret"
```

For details on how readers and writers work, and how to add your own, see [CLAUDE.md](CLAUDE.md#architecture).
