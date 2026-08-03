# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

StreamCables connects to audio stream metadata sources (icecast/shoutcast "now playing" info) and publishes it to other places (stdout, Twitter). It's a plugin-style reader/writer tool, not a library.

## Commands

```
uv sync   # make init
uv run python streamcables/streamcables.py   # make run
```

There is no test suite, linter config, or CI beyond dependabot auto-merge (`.github/workflows/dependabot-auto-merge.yml`). `pylint` and `black` are dev dependencies (`[dependency-groups] dev` in `pyproject.toml`) but have no invocation wired up.

Requires Python 3.11+ (see `pyproject.toml`), and imports are unqualified (`import settings`, not `from streamcables import settings`) — the package relies on `streamcables/` itself being on `sys.path` when run as a script, not on being installed.

## Architecture

Everything is a plugin loaded by name from `settings.toml`, resolved dynamically in `streamcables.py:plugins()`:

- `config["main"]["reader"]` names one module (e.g. `icecast`) whose `register()` function is called.
- `config["main"]["writers"]` names one or more modules (e.g. `stdout`, `twitter`) whose `register()` functions are each called.
- Each plugin module's `register()` returns a callable — the reader's callable takes no args and returns an `info` dict with at least `hash` and `now` keys; each writer's callable takes that `info` dict.
- The main loop (`streamcables.py:main`) polls the reader on `refresh-rate` (seconds), and only invokes the writers when `info["hash"]` changes from the last poll — this is how track changes are detected and deduped.
- A plugin that isn't installed/importable is skipped with a warning rather than crashing the run (see the `NotImplementedError` catch in `plugins()` — new plugins should follow the existing modules' `register()`/`NotImplementedError` convention to fit this).

To add a new reader or writer, add a module at `streamcables/<name>.py` exposing `register()`, and reference `<name>` in `settings.toml`.

Existing plugins:
- `icecast.py` — reader; scrapes an icecast `status.xsl` page with BeautifulSoup for the currently-playing track.
- `stdout.py` — writer; prints to the screen.
- `twitter.py` — writer; posts to Twitter via tweepy, handling OAuth token storage/refresh under the user's app data dir.

## Settings

Config is TOML, loaded by `settings.py:init()` from an OS-specific app data dir (via `appdirs.AppDirs("StreamCables", "NoNoTools")`), not from the repo. If the file doesn't exist, it's copied from `settings.default.toml` and the process exits, prompting the user to edit it and rerun. See `README.md` for the settings file format (`[main]`, `[icecast]`, `[twitter]` sections).
