import logging

logger = logging.getLogger()

if not logger.hasHandlers():
    handler = logging.FileHandler('shipments.log', mode='w')
    formatter = logging.Formatter('%(levelname)s %(message)s')

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)


class Cargo:
    def __init__(self, destination, weight):
        self.destination = destination
        self.weight = weight
        logger.info(f"[Cargo] initialized: {self.__repr__()}")

    def __str__(self):
        return f"Cargo to {self.destination} with weight {self.weight}"

    def __repr__(self):
        return f"Cargo(destination={self.destination}, weight={self.weight})"


class Container:
    def __init__(self, weight_limit, cargo=None):
        self.weight_limit = weight_limit
        if cargo and cargo.weight <= self.weight_limit:
            self.set_cargo(cargo)
        else:
            self.cargo = None
        logger.info(f"[Container] initialized: {self.__repr__()}")

    def set_cargo(self, other):
        if other.weight <= self.weight_limit:
            self.cargo = other
            logger.info(f"[Container] Cargo set: {self.cargo}")

    def __str__(self):
        return f"Container up to {self.weight_limit} with {self.cargo}"

    def __repr__(self):
        return f"Container(weight_limit={self.weight_limit}, cargo={repr(self.cargo)})"

class Ship:
    def __init__(self, route, containers):
        self.route = route
        self.containers = []
        self.add_containers(containers)
        logger.info(f"[Ship] initialized: {repr(self)}")

    def add_containers(self, conts):
        for c in conts:
            if c.cargo and c.cargo.destination in self.route:
                self.containers.append(c)
                logger.info(f"[Ship] Added Container: {c}")

    def __str__(self):
        tmp = f"Ship to {self.route} with containers:"
        for c in self.containers:
            tmp += '\n' + str(c)
        return tmp

    def __repr__(self):
        return f"Ship(route={self.route}, containers={repr(self.containers)})"
