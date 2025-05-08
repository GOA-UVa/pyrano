"""Use cases related to interacting with instrument data files"""
from datetime import datetime, timedelta

import pandas as pd

from pyrano.data_access import raw
from pyrano.common.config import ClientConfig

def read_last(last_hours: float, cfg: ClientConfig) -> pd.DataFrame:
    last = datetime.now()
    first = last - timedelta(hours=last_hours)
    df = raw.read_data_between(first, last, cfg.storage)
    df["station"] = cfg.measurement.station
    df["instr_id"] = cfg.measurement.instr_id
    df["install_time"] = pd.to_datetime(cfg.measurement.install_time)
    return df
