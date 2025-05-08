"""Use cases related to interacting with instrument data files"""
from datetime import datetime, timedelta

import pandas as pd

from pyrano.data_access import db, raw
from pyrano.common.config import get_config
from pyrano.common.constants import CONFIG_DEFAULT_PATH

def read_send_last(last_hours: float, config_path: str = CONFIG_DEFAULT_PATH):
    cfg = get_config(config_path)
    last = datetime.now()
    first = last - timedelta(hours=last_hours)
    df = raw.read_data_between(first, last, cfg.storage)
    df["station"] = cfg.database.station
    df["instr_id"] = cfg.database.instr_id
    df["installed_at"] = pd.to_datetime(cfg.database.installed_at)
    db.insert_df(df, cfg.database, "measurement")
