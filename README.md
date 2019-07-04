# Introduction

StreamCables, on the most basic level, is a tool that connects to audio streams and sends information to other place. It's been primarily written to connect to icecast and shoutcast streams, and stream tracklists to social media. However, it can connect read and write to multiple services, and is written for extensibility. 

Currently it supports these readers:

  - icecast

Currently it supports these writers:

  - stdout (the screen)
  - Twitter

Feel free to submit a pull request if your workflow is missing.

# Prerequisites

On OpenSUSE Tumbleweed the python development libraries must be installed to compile 
StreamCables' dependencies:

```
sudo zypper install gcc
sudo zypper install python3-devel-3.6.5-3.3
```

# Setup

StreamCables requires  [Python 3.6, pip and pipenv](https://docs.python-guide.org/). 
Installation:

```
git clone <repository url> streamcables
cd streamcables
pipenv install
```

Run the program as follows:

```
pipenv run python streamcables/streamcables.py
# shorter version
make run
```

# Settings and Configuration

You will be asked to create a settings file, the location will be printed to the screen if it doesn't exist. This settings file must contain one reader and one or more writers. To use Twitter functionality, a registered Twitter developer account and application is required which provides the key and secret.

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

# readers

Readers must return a dict containing hash and now
