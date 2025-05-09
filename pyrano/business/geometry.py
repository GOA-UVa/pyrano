import pandas as pd
from pvlib import solarposition


def filter_solar_day(df, lat, lon) -> pd.DataFrame:
    solpos = solarposition.get_solarposition(df["measured_at"], lat, lon)
    df = df[solpos['apparent_elevation'] > 0]
    return df
