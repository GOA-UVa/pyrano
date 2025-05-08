"""This module is in charge of logging the output data."""

import logging
from datetime import datetime, timezone
import os

from pyrano.common.models import LogConfig
from pyrano.common import constants

# SINGLETON
_logger: logging.Logger = None

_FORMAT = "%(levelname)s: %(asctime)s - [%(filename)s:%(lineno)s - %(funcName)10s() ] %(message)s"
_DATEFORMAT = "%H:%M:%S"


def get_logger(cfg: LogConfig) -> logging.Logger:
    """Returns the system's logger

    :return: System's logger
    :rtype: logging.Logger
    """
    global _logger
    if _logger is None:
        dtnow = datetime.now(timezone.utc)
        logname = dtnow.strftime("%Y%m%d")
        logname = "log_{}.txt".format(logname)
        os.makedirs(cfg.logdir, exist_ok=True)
        logname = os.path.join(cfg.logdir, logname)
        logging.basicConfig(
            filename=logname, filemode="a", format=_FORMAT, datefmt=_DATEFORMAT
        )
        _logger = logging.getLogger(__name__)
        debug_value = "INFO"
        if constants.DEBUG_ENV_NAME in os.environ:
            debug_value = os.environ[constants.DEBUG_ENV_NAME]
        if cfg.debug:
            debug_value = "DEBUG"
        if isinstance(debug_value, str) and debug_value.upper() == "DEBUG":
            _logger.setLevel(logging.DEBUG)
        else:
            _logger.setLevel(logging.INFO)

    return _logger
