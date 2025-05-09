from datetime import datetime, timezone

from pyrano.business import data, plots, geometry
from pyrano.common.config import get_server_config
from pyrano.common.constants import SERVER_CONFIG_DEFAULT_PATH

def plot_last_hours(last_hours: float, station: str, plotpath: str, config_path = SERVER_CONFIG_DEFAULT_PATH):
    cfg = get_server_config(config_path)
    df = data.get_last_measurements(last_hours, station, cfg)
    plots.plot_measurements(df, plotpath)

def plot_today(station: str, plotpath: str, config_path = SERVER_CONFIG_DEFAULT_PATH):
    cfg = get_server_config(config_path)
    dfstat = data.get_station(station, cfg)
    df = data.get_utctoday_measurements(station, cfg)
    lat = dfstat['latitude'].values[0]
    lon = dfstat['longitude'].values[0]
    dt0, dtf = geometry.get_solar_day_lims(datetime.now(), lat, lon)
    plots.plot_measurements(df, plotpath, (dt0, dtf))
