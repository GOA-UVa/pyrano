"""Interacting with the system sql database"""
import pandas as pd
from goadb.sql import DBConfig, insert_dataframe as _insdf

def insert_df(df: pd.DataFrame, config: DBConfig, table: str):
    _insdf(df, config, table)
