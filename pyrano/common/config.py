"""
Get global configuration parameters.
"""
from pathlib import Path
import os
from dataclasses import dataclass, asdict

import yaml

from pyrano.common.models import (
    StorageSettings,
    DBConfig,
)
from pyrano.common.constants import CONFIG_DEFAULT_PATH

# Singleton configuration value
_config = None


@dataclass
class Config:
    storage: StorageSettings
    database: DBConfig

    def store_to_yml(self, path: str):
        with open(path, "w", encoding="utf-8") as ymlfile:
            yaml.safe_dump(asdict(self), ymlfile)


def _read_config_from_file(path: str) -> Config:
    with open(path, encoding="utf-8") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    storage = StorageSettings(**cfg["storage"])
    db = DBConfig(**cfg["database"])
    config = Config(storage, db)
    return config


def _init_config(path: str):
    """Store in each mutable the values from the parameters file to be used in other functions."""
    global _config
    base = Path().absolute()
    if not os.path.exists(path):
        path = os.path.join(base, "config.test.yml")
    _config = _read_config_from_file(path)


def get_config(config_path=CONFIG_DEFAULT_PATH) -> Config:
    """
    Read the system mutable params and return them.

    :return: the system global configuration params.
    :rtype: Config
    """
    if _config is None:
        _init_config(config_path)
    return _config


def get_default_config() -> Config:
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(curr_dir, "assets", "config.test.yml")
    return _read_config_from_file(path)
