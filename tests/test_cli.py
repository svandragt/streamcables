import os
import subprocess
import sys


def test_first_run_creates_settings_file(tmp_path):
    env = {**os.environ, "XDG_DATA_HOME": str(tmp_path)}

    result = subprocess.run(
        [sys.executable, "-m", "streamcables.streamcables"],
        check=False,
        cwd=tmp_path,
        env=env,
        capture_output=True,
        text=True,
    )

    assert (tmp_path / "StreamCables" / "settings.toml").exists()
    assert "Traceback" not in result.stderr
