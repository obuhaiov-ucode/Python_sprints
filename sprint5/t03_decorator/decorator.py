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
    def inner(*args):
        res = func(*args)

        logger.info(f"<{type(args[0]).__name__}>: - {func.__name__} method has been called.")

        return res
    return inner

class Cargo:
    @log
    def __init__(self, destination, weight):
        self.destination = destination
        self.weight = weight

    @log
    def __str__(self):
        return f"Cargo to {self.destination} with weight {self.weight}"

    @log
    def __repr__(self):
        return f"Cargo(destination={self.destination}, weight={self.weight})"

class Container:
    @log
    def __init__(self, weight_limit, cargo=None):
        self.weight_limit = weight_limit
        self.set_cargo(cargo)

    @log
    def set_cargo(self, other):
        if other and other.weight <= self.weight_limit:
            self.cargo = other
        else:
            self.cargo = None

    @log
    def __str__(self):
        return f"Container up to {self.weight_limit} with {self.cargo}"

    @log
    def __repr__(self):
        return f"Container(weight_limit={self.weight_limit}, cargo={repr(self.cargo)})"

class Ship:
    @log
    def __init__(self, route, containers):
        self.route = route
        self.containers = []
        self.add_containers(containers)

    @log
    def add_containers(self, conts):
        for c in conts:
            if c.cargo and c.cargo.destination in self.route:
                self.containers.append(c)

    @log
    def __str__(self):
        tmp = f"Ship to {self.route} with containers:"
        for c in self.containers:
            tmp += '\n' + str(c)
        return tmp

    @log
    def __repr__(self):
        return f"Ship(route={self.route}, containers={repr(self.containers)})"
