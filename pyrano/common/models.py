from dataclasses import dataclass
from datetime import datetime

@dataclass
class MeasurementConfig:
    station: str
    instr_id: str
    install_time: datetime

@dataclass
class StorageSettings:
    output_dir: str

@dataclass
class LogConfig:
    logdir: str
    debug: bool

@dataclass
class SecureConfig:
    x_api_key: str

@dataclass
class ClientServerConfig:
    url: str
    x_api_key: str

@dataclass
class UrlConfig:
    root_path: str
