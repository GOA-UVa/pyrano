"""Read data from pyranometer ouput files"""
import os
from datetime import datetime, timedelta

import pandas as pd

from pyrano.common.models import StorageSettings

_BASECOLS = ["date", "time", "radiation", "temp", "voltage"]

def read_file(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, sep=';', skiprows=1, usecols=[1,2,3,4,5], names=[_BASECOLS])
    df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'])
    df = df.drop(columns=['date', 'time'])
    return df


def read_data_between(first: datetime, last: datetime, conf: StorageSettings) -> pd.DataFrame:
    firstname = first.strftime("LOG%y%m%d")
    lastname = (last + timedelta(1)).strftime("LOG%y%m%d")
    files = [f for f in os.listdir(conf.output_dir) if firstname <= f <=lastname]
    dfs = []
    for f in files:
        dfs.append(read_file(os.path.join(conf.output_dir, f)))
    df = pd.concat(dfs)
    df = df[(df['datetime'].dt >= first) & (df['datetime'].dt <= last)]
    return df
