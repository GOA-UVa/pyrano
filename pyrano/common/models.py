from dataclasses import dataclass
from datetime import datetime

from goadb.sql import DBConfig as _DBConfig

@dataclass
class DBConfig(_DBConfig):
    username: str
    password: str
    host: str
    database: str

@dataclass
class MeasurementConfig:
    station: str
    instr_id: str
    install_time: datetime

@dataclass
class StorageSettings:
    output_dir: str

@dataclass
class ClientServerConfig:
    url: str
