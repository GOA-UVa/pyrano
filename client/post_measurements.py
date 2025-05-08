from urllib.parse import urljoin

import pandas as pd
import requests

from pyrano.business.measurement import read_last
from pyrano.common.config import get_client_config
from pyrano.common.constants import CLIENT_CONFIG_DEFAULT_PATH

def _post_measurements(df: pd.DataFrame, api_url="http://localhost:8000/measurements"):
    df["install_time"] = pd.to_datetime(df["install_time"]).dt.strftime('%Y-%m-%dT%H:%M:%S')
    df["measured_at"] = pd.to_datetime(df["measured_at"]).dt.strftime('%Y-%m-%dT%H:%M:%S')

    payload = df.to_dict(orient="records")

    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()
        print(f"[OK] Inserted {response.json().get('inserted')} measurements.")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Insertion failed: {e}")


def _join_url(a: str, b: str):
    if not a.endswith('/'):
        a = f'{a}/'
    return urljoin(a, b)

def read_post(last_hours: float, config_path = CLIENT_CONFIG_DEFAULT_PATH):
    cfg = get_client_config(config_path)
    df = read_last(last_hours, cfg)
    _post_measurements(df, _join_url(cfg.server.url, "measurements"))
