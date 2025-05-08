from typing import List
import os

from matplotlib.axes import Axes
from matplotlib import dates as mdates
import pandas as pd

_FIGSIZE = (12, 6)

def _finish_plot(axes: List[Axes], path: str):
    ax = axes[0]
    ax.set_axisbelow(True)
    ax.grid()
    locator = mdates.AutoDateLocator(minticks=3, maxticks=12)
    formatter = mdates.ConciseDateFormatter(locator)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    ax.margins(x=0.01)
    fig = ax.get_figure()
    for ax in axes:
        leg = ax.get_legend()
        if leg:
            ax.get_legend().remove()
    fig.tight_layout()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fig.savefig(path)

def plot_measurements(df: pd.DataFrame, path: str):
    ax = df.plot.scatter('measured_at', 'value', 8, "orange", figsize=_FIGSIZE)
    ax.set_ylabel("Radiation (W/m²)")
    ax.set_xlabel("Date")
    _finish_plot([ax], path)
