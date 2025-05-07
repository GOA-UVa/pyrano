from dataclasses import dataclass
from datetime import datetime

from goadb.sql import DBConfig as _DBConfig

@dataclass
class DBConfig(_DBConfig):
    username: str
    password: str
    host: str
    database: str
    station: str
    instr_id: str
    installed_at: datetime

@dataclass
class StorageSettings:
    output_dir: str
