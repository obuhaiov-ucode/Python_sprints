import logging
import sys

from .names import names
from .titles import titles

logger = logging.getLogger()

if not logger.hasHandlers():
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        '..::Knight Generator::.. %(process)d-%(levelname)s-%(message)s')

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    logger.info("Package __init__ executed.")

from .__init__ import logger
