from pathlib import Path

import pytest
import settings

DEFAULT_SETTINGS = Path(__file__).parent.parent / "settings.default.toml"


class FakeDirs:
    def __init__(self, path):
        self.user_data_dir = str(path)


def test_init_reads_existing_settings(tmp_path, monkeypatch):
    (tmp_path / "settings.toml").write_text('[main]\nreader = "icecast"\n')
    monkeypatch.setattr(settings, "AppDirs", lambda *a, **k: FakeDirs(tmp_path))

    settings.init()

    assert settings.config["main"]["reader"] == "icecast"


def test_init_creates_default_settings_when_missing(tmp_path, monkeypatch):
    user_data_dir = tmp_path / "nested" / "does-not-exist-yet"
    monkeypatch.setattr(settings, "AppDirs", lambda *a, **k: FakeDirs(user_data_dir))

    with pytest.raises(SystemExit):
        settings.init()

    created = user_data_dir / "settings.toml"
    assert created.read_text() == DEFAULT_SETTINGS.read_text()
