"""Read data from pyranometer ouput files"""
import os
from datetime import datetime, timedelta
from io import StringIO
from typing import Union

import pandas as pd

from pyrano.common.models import StorageSettings

_BASECOLS = ["date", "time", "radiation", "temp", "voltage"]

def read_file(path: str) -> Union[pd.DataFrame, None]:
    with open(path, encoding="utf-8") as f:
        lines = [line for line in f if line.startswith(".data")]
    lines = [line for line in lines if line.count(';') > 5]
    if not lines:
        return None
    csvdata = StringIO("\n".join(lines))
    df = pd.read_csv(csvdata, sep=';', usecols=[1,2,3,4,5], names=_BASECOLS)
    df['measured_at'] = pd.to_datetime(df['date'] + ' ' + df['time'])
    df = df.drop(columns=['date', 'time'])
    df = df[df['radiation'].notna()]
    return df


def read_data_between(first: datetime, last: datetime, conf: StorageSettings) -> pd.DataFrame:
    firstname = first.strftime("LOG%y%m%d")
    lastname = (last + timedelta(1)).strftime("LOG%y%m%d")
    files = [f for f in os.listdir(conf.output_dir) if firstname <= f <=lastname]
    dfs = []
    for f in files:
        dfs.append(read_file(os.path.join(conf.output_dir, f)))
    dfs = [df for df in dfs if df is not None and not df.empty]
    df = pd.concat(dfs)
    df = df[(df['measured_at'] >= first) & (df['measured_at'] <= last)]
    df = df.drop(columns=["voltage"])
    df = df.rename(columns={'radiation': 'value'})
    return df
