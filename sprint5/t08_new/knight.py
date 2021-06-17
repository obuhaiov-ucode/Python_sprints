import logging
import sys

logger = logging.getLogger()

if not logger.hasHandlers():
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(levelname)s %(message)s')

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

def log(func):
    def inner(*args, **kwargs):
        logger.info(f"{func.__name__} with {kwargs}")

        return func(*args, **kwargs)
    return inner

class Knight:
    counter = 0
    instances = []

    @log
    def __new__(cls, **kwargs):
        if cls.counter > 3:
            logger.error("Cannot create a Knight. The Round Table can only fit 4 Knights.")
            return None
        if kwargs.get("name") == "Arthur":
            logger.error("Cannot create a Knight with the name Arthur. Arthur is the King.")
            return None
        for key, value in kwargs.items():
            setattr(cls, key, value)
        cls.counter += 1
        return object.__new__(cls)

    @log
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.instances.append(self)
