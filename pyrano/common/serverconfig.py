"""
Get server configuration parameters.
"""
from pathlib import Path
import os
from dataclasses import dataclass, asdict

import yaml
from goadb.sql import DBConfig as _DBConfig

from pyrano.common.models import (
    UrlConfig,
    LogConfig,
    SecureConfig,
)
from pyrano.common.constants import SERVER_CONFIG_DEFAULT_PATH


# Singleton
_server_config = None


@dataclass
class DBConfig(_DBConfig):
    username: str
    password: str
    host: str
    database: str


@dataclass
class ServerConfig:
    database: DBConfig
    url: UrlConfig
    log: LogConfig
    secure: SecureConfig

    def store_to_yml(self, path: str):
        with open(path, "w", encoding="utf-8") as ymlfile:
            yaml.safe_dump(asdict(self), ymlfile)

def _read_server_config_from_file(path: str) -> ServerConfig:
    with open(path, encoding="utf-8") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    db = DBConfig(**cfg["database"])
    url = UrlConfig(**cfg["url"])
    log = LogConfig(**cfg['log'])
    secure = SecureConfig(**cfg['secure'])
    config = ServerConfig(db, url, log, secure)
    return config

def _init_server_config(path: str):
    """Store in each mutable the values from the parameters file to be used in other functions."""
    global _server_config
    base = Path().absolute()
    if not os.path.exists(path):
        path = os.path.join(base, "serverconf.test.yml")
    _server_config = _read_server_config_from_file(path)

def get_server_config(config_path=SERVER_CONFIG_DEFAULT_PATH) -> ServerConfig:
    """
    Read the system server mutable params and return them.

    :return: the system global configuration params.
    :rtype: ServerConfig
    """
    if _server_config is None:
        _init_server_config(config_path)
    return _server_config
