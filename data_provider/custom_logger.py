import os
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('data_provider')
logger.setLevel(logging.DEBUG)
fh=RotatingFileHandler(os.path.join("logs/", "main.log"), maxBytes=2e6, backupCount=100)
fh.setFormatter(logging.Formatter("[%(asctime)s] [%(levelname)s] [%(name)s->%(funcName)s->L%(lineno)d] %(message)s"))
logger.addHandler(fh)

