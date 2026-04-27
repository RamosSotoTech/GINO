"""Project settings and runtime configuration.

This module keeps fallback defaults and saved user configuration in one place
without depending on PyGame. Runtime code can load ``GameConfig`` at startup,
and a future settings scene can save changes back to disk.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
import os
from pathlib import Path
import sys

APP_NAME = "gino"

DEFAULT_WIDTH = 1280
DEFAULT_HEIGHT = 720
DEFAULT_FPS = 60
DEFAULT_FULLSCREEN = False
DEFAULT_MASTER_VOLUME = 1.0


@dataclass
class GameConfig:
    """User-adjustable game configuration."""

    width: int = DEFAULT_WIDTH
    height: int = DEFAULT_HEIGHT
    fps: int = DEFAULT_FPS
    fullscreen: bool = DEFAULT_FULLSCREEN
    master_volume: float = DEFAULT_MASTER_VOLUME


def get_config_dir() -> Path:
    """Return the platform-appropriate folder for user config files."""
    if sys.platform == "win32":
        base_path = Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming"))
        return base_path / "GINO"

    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "GINO"

    base_path = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config"))
    return base_path / APP_NAME


CONFIG_PATH = get_config_dir() / "settings.json"


def load_config(config_path: Path = CONFIG_PATH) -> GameConfig:
    """Load saved user settings, falling back to defaults when needed."""
    if not config_path.exists():
        return GameConfig()

    try:
        with config_path.open("r", encoding="utf-8") as config_file:
            data = json.load(config_file)
    except (OSError, json.JSONDecodeError):
        return GameConfig()

    return GameConfig(
        width=_read_int(data, "width", DEFAULT_WIDTH, minimum=320),
        height=_read_int(data, "height", DEFAULT_HEIGHT, minimum=240),
        fps=_read_int(data, "fps", DEFAULT_FPS, minimum=1),
        fullscreen=_read_bool(data, "fullscreen", DEFAULT_FULLSCREEN),
        master_volume=_read_float(
            data,
            "master_volume",
            DEFAULT_MASTER_VOLUME,
            minimum=0.0,
            maximum=1.0,
        ),
    )


def save_config(config: GameConfig, config_path: Path = CONFIG_PATH) -> None:
    """Save user settings to disk."""
    config_path.parent.mkdir(parents=True, exist_ok=True)
    with config_path.open("w", encoding="utf-8") as config_file:
        json.dump(asdict(config), config_file, indent=2)
        config_file.write("\n")


def _read_bool(data: dict[str, object], key: str, default: bool) -> bool:
    """Read a boolean from JSON-like data."""
    value = data.get(key, default)
    if isinstance(value, bool):
        return value
    return default


def _read_float(
    data: dict[str, object],
    key: str,
    default: float,
    minimum: float,
    maximum: float,
) -> float:
    """Read and clamp a float from JSON-like data."""
    try:
        value = float(data.get(key, default))
    except (TypeError, ValueError):
        return default

    return max(minimum, min(maximum, value))


def _read_int(
    data: dict[str, object],
    key: str,
    default: int,
    minimum: int,
) -> int:
    """Read a bounded integer from JSON-like data."""
    try:
        value = int(data.get(key, default))
    except (TypeError, ValueError):
        return default

    return max(minimum, value)
