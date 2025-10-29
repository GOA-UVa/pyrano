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
    ClientServerConfig,
    MeasurementConfig,
    UrlConfig,
    LogConfig,
    SecureConfig,
)
from pyrano.common.constants import CLIENT_CONFIG_DEFAULT_PATH, SERVER_CONFIG_DEFAULT_PATH

# Singleton configuration values
_client_config = None
_server_config = None


@dataclass
class ClientConfig:
    storage: StorageSettings
    measurement: MeasurementConfig
    server: ClientServerConfig
    log: LogConfig

    def store_to_yml(self, path: str):
        with open(path, "w", encoding="utf-8") as ymlfile:
            yaml.safe_dump(asdict(self), ymlfile)

def _read_client_config_from_file(path: str) -> ClientConfig:
    with open(path, encoding="utf-8") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    storage = StorageSettings(**cfg["storage"])
    meas = MeasurementConfig(**cfg["measurement"])
    sv = ClientServerConfig(**cfg["server"])
    log = LogConfig(**cfg['log'])
    config = ClientConfig(storage, meas, sv, log)
    return config


def _init_client_config(path: str):
    """Store in each mutable the values from the parameters file to be used in other functions."""
    global _client_config
    base = Path().absolute()
    if not os.path.exists(path):
        path = os.path.join(base, "config.test.yml")
    _client_config = _read_client_config_from_file(path)


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

def get_client_config(config_path=CLIENT_CONFIG_DEFAULT_PATH) -> ClientConfig:
    """
    Read the system client mutable params and return them.

    :return: the system global configuration params.
    :rtype: ClientConfig
    """
    if _client_config is None:
        _init_client_config(config_path)
    return _client_config

def get_server_config(config_path=SERVER_CONFIG_DEFAULT_PATH) -> ServerConfig:
    """
    Read the system server mutable params and return them.

    :return: the system global configuration params.
    :rtype: ServerConfig
    """
    if _server_config is None:
        _init_server_config(config_path)
    return _server_config
