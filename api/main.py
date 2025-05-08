from pydantic import BaseModel
from typing import List
from datetime import datetime

from fastapi import FastAPI, HTTPException
import pandas as pd

from pyrano.data_access.db import insert_df
from pyrano.common.config import get_server_config
from pyrano.common.constants import SERVER_CONFIG_DEFAULT_PATH

cfg = get_server_config(SERVER_CONFIG_DEFAULT_PATH)
app = FastAPI(root_path=cfg.url.root_path)

class Measurement(BaseModel):
    station: str
    instr_id: str
    install_time: datetime
    measured_at: datetime
    value: float

@app.post("/measurements")
def add_measurements(measurements: List[Measurement]):
    config_path = SERVER_CONFIG_DEFAULT_PATH
    cfg = get_server_config(config_path)
    try:
        records = [m.model_dump() for m in measurements]
        df = pd.DataFrame(records)
        inserted = insert_df(df, cfg.database, "measurement")
        return {"inserted": inserted}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
