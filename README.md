# Introduction

StreamCables, on the most basic level, is a tool that connects to audio streams and sends information to other place. It's been primarily written to connect to icecast and shoutcast streams, and stream tracklists to social media. However, it can connect to a single reader, and multiple writers, and is written for extensibility. 

Currently it supports these readers:

  - icecast

Currently it supports these writers:

  - stdout (the screen)
  - twitter

Feel free to submit a pull request if your workflow is missing.

# Prerequisites

On OpenSUSE Tumbleweed the following packages are required in order to compile 
python dependencies:

```
sudo zypper install gcc
sudo zypper install python3-devel-3.6.5-3.3
```

# Setup

StreamCables requires  [Python 3.6, its development libraries, pip and pipenv](https://docs.python-guide.org/). 
Developers can install it as follows:

```
git clone <repository url> streamcables
cd streamcables
pipenv install
```

Run the program as follows:

```
pipenv run ./streamcables.py
```

You will also need a settings file (next section). 

# settings.toml

Example settings:

```
[main]
reader = 'icecast'
writers = ['stdout', 'twitter']
refresh-rate = 20

[icecast]
url="http://listen.snowcloudfm.com:8000/status.xsl"

```

# readers

Readers must return a dict containing hash and now
