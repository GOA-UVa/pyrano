from datetime import datetime, timedelta

import pandas as pd

from pyrano.common.config import ServerConfig
from pyrano.data_access.db import get_measurements_between

def get_last_measurements(last_hours: float, station: str, cfg: ServerConfig) -> pd.DataFrame:
    now = datetime.now()
    df = get_measurements_between(cfg.database, station, now-timedelta(hours=last_hours), now)
    return df
