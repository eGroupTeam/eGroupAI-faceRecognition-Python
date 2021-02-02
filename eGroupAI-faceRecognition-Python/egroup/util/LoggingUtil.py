# =================================SETTING FOR LOGGING==================================================================
# config formatter
import logging
import os.path as osp
from datetime import date
LOG_HOME = "C:/logs"
APP_NAME = "FacePass"

LOGGER_FORMATTER = logging.Formatter(fmt="%(asctime)s %(levelname)s %(filename)s - %(message)s",
                                     datefmt="%Y-%m-%d %H:%M:%S,%z")

# config logging file
FILE_HANDLER = logging.FileHandler(filename=osp.join(LOG_HOME, f"{APP_NAME}.{date.today().isoformat()}-python.log"),
                                   mode="a", )
FILE_HANDLER.setFormatter(LOGGER_FORMATTER)

# config logging console
CONSOLE_HANDLER = logging.StreamHandler()
CONSOLE_HANDLER.setFormatter(LOGGER_FORMATTER)

LOGGER = logging.getLogger()

LOGGER.setLevel(logging.INFO)

# attach config to the logger
LOGGER.addHandler(FILE_HANDLER)
LOGGER.addHandler(CONSOLE_HANDLER)
# =================================END SETTING FOR LOGGING==============================================================
