import logging

import arg


def test_default_loglevel(monkeypatch):
    monkeypatch.setattr("sys.argv", ["prog"])
    assert arg.parse().loglevel == logging.WARNING


def test_verbose_flag(monkeypatch):
    monkeypatch.setattr("sys.argv", ["prog", "-v"])
    assert arg.parse().loglevel == logging.INFO


def test_debug_flag(monkeypatch):
    monkeypatch.setattr("sys.argv", ["prog", "-d"])
    assert arg.parse().loglevel == logging.DEBUG
