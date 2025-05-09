"""Interacting with the system sql database"""
from datetime import datetime

import pandas as pd

from goadb.sql import DBConfig, DataBase, insert_dataframe as _insdf

def insert_df(df: pd.DataFrame, config: DBConfig, table: str) -> int:
    return _insdf(df, config, table)

_SQL_DT = "%Y-%m-%d %H:%M:%S"

def get_measurements_between(config: DBConfig, station: str, first: datetime, last: datetime) -> pd.DataFrame:
    db = DataBase(config)
    df = db.run_query(
        (
            f"SELECT * FROM measurement WHERE station = '{station}' AND "
            f"measured_at BETWEEN '{first.strftime(_SQL_DT)}' AND '{last.strftime(_SQL_DT)}'"
        )
    )
    return df


def get_station(config: DBConfig, station: str) -> pd.DataFrame:
    db = DataBase(config)
    df = db.run_query(f"SELECT * FROM site WHERE station = '{station}'")
    return df
