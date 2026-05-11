from datetime import datetime, timedelta, timezone

import pandas as pd

from pyrano.common.serverconfig import ServerConfig
from pyrano.data_access.db import get_measurements_between, get_station as _gstat

def get_last_measurements(last_hours: float, station: str, cfg: ServerConfig) -> pd.DataFrame:
    now = datetime.now()
    df = get_measurements_between(cfg.database, station, now-timedelta(hours=last_hours), now)
    return df


def get_utctoday_measurements(station: str, cfg: ServerConfig) -> pd.DataFrame:
    now = datetime.now(timezone.utc)
    now0 = datetime(now.year, now.month, now.day, 0, 0, 0, tzinfo=timezone.utc)
    df = get_measurements_between(cfg.database, station, now0, now)
    return df


def get_station(station: str, cfg: ServerConfig) -> pd.DataFrame:
    return _gstat(cfg.database, station)
