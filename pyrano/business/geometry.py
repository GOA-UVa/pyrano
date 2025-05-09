from typing import Tuple
from datetime import datetime, timezone, timedelta

import pandas as pd
from pvlib import solarposition

def get_solar_day_lims(dt: datetime, lat: float, lon: float) -> Tuple[datetime, datetime]:
    dt0 = datetime(dt.year, dt.month, dt.day, 0, 0, 0, tzinfo=timezone.utc)
    dtr = pd.date_range(dt0, dt0+timedelta(1), freq=timedelta(minutes=15))
    solpos = solarposition.get_solarposition(dtr, lat, lon)
    mask = solpos['apparent_elevation'].values > 0
    return dtr[mask][0], dtr[mask][-1]

def filter_solar_day(df, lat, lon) -> pd.DataFrame:
    solpos = solarposition.get_solarposition(df["measured_at"], lat, lon)
    df = df[solpos['apparent_elevation'].values > 0]
    return df
