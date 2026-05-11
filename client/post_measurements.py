from urllib.parse import urljoin

import pandas as pd
import requests

from pyrano.business.measurement import read_last
from pyrano.common.clientconfig import get_client_config
from pyrano.common.constants import CLIENT_CONFIG_DEFAULT_PATH
from pyrano.common.logger import get_logger

def _post_measurements(df: pd.DataFrame, api_url="http://localhost:8000/measurements", config_path = CLIENT_CONFIG_DEFAULT_PATH):
    df["install_time"] = pd.to_datetime(df["install_time"]).dt.strftime('%Y-%m-%dT%H:%M:%S')
    df["measured_at"] = pd.to_datetime(df["measured_at"]).dt.strftime('%Y-%m-%dT%H:%M:%S')

    payload = df.to_dict(orient="records")
    cfg = get_client_config(config_path)
    log = get_logger(cfg.log)
    headers = {"X-API-Key": cfg.server.x_api_key}

    try:
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()
        msg = f"[OK] Inserted {response.json().get('inserted')} measurements."
        log.debug(msg)
        print(msg)
    except requests.exceptions.RequestException as e:
        msg = f"[ERROR] Insertion failed: {str(e)}"
        print(msg)
        log.error(msg)


def _join_url(a: str, b: str):
    if not a.endswith('/'):
        a = f'{a}/'
    return urljoin(a, b)

def read_post(last_hours: float, config_path = CLIENT_CONFIG_DEFAULT_PATH):
    cfg = get_client_config(config_path)
    df = read_last(last_hours, cfg)
    _post_measurements(df, _join_url(cfg.server.url, "measurements"), config_path)
