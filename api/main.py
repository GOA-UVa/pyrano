from pydantic import BaseModel
from typing import List
from datetime import datetime

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import pandas as pd

from pyrano.data_access.db import insert_df
from pyrano.common.serverconfig import get_server_config
from pyrano.common.logger import get_logger
from pyrano.common.constants import SERVER_CONFIG_DEFAULT_PATH

cfg = get_server_config(SERVER_CONFIG_DEFAULT_PATH)
app = FastAPI(root_path=cfg.url.root_path)

class Measurement(BaseModel):
    station: str
    instr_id: str
    install_time: datetime
    measured_at: datetime
    value: float
    temp: float


API_KEY = cfg.secure.x_api_key

@app.middleware("http")
async def verify_api_key(request: Request, call_next):
    key = request.headers.get("X-API-Key")
    if key != API_KEY:
        client_host = request.client.host if request.client else "unknown"
        method = request.method
        path = request.url.path
        shown_key = key[:4] + "..." if key else "None"
        get_logger(cfg.log).warning(
            "Unauthorized request: IP=%s method=%s path=%s key=%s",
            client_host, method, path, shown_key,
        )
        return JSONResponse(status_code=401, content={"detail": "Invalid or missing API key"})
    response = await call_next(request)
    return response

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
        get_logger(cfg.log).critical(str(e))
        return JSONResponse(status_code=500, content={"detail": str(e)})
