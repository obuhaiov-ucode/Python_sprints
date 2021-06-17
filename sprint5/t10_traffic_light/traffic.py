import sys
import logging
import time

clr = ['\033[1;32m',  # Green
       '\033[1;31m',  # Red
       '\033[1;33m',   # Yellow
       '\033[m']

logger = logging.getLogger()

if not logger.hasHandlers():
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(levelname)s %(message)s')

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

class TrafficLightState:
    def get_new_color(self):
        prev_char = ''
        while True:
            char = yield
            if char == 'y' and prev_char == 'r':
                self.state = self.green
            if char == 'y' and prev_char == 'g':
                self.state = self.red
            if char == 'g' or char == 'r':
                self.state = self.yellow
            prev_char = char

class TrafficLightStateMachine(TrafficLightState):
    def __init__(self):
        super(TrafficLightStateMachine, self).__init__()
        self.green = GreenState()
        self.red = RedState()
        self.yellow = YellowState()
        self.state = self.green
        self.get = self.get_new_color()
        self.get.send(None)
        logger.info("TrafficLight state machine created")

    def __call__(self):
        while True:
            yield self.state.color
            self.get.send(self.state.c)
            time.sleep(0.2)


class GreenState(TrafficLightState):
    def __init__(self):
        super(GreenState, self).__init__()
        self.color = f'{clr[0]}Green{clr[3]}'
        self.c = 'g'
        logger.info("GreenState created")

class RedState(TrafficLightState):
    def __init__(self):
        super(RedState, self).__init__()
        self.color = f'{clr[1]}Red{clr[3]}'
        self.c = 'r'
        logger.info("RedState created")

class YellowState(TrafficLightState):
    def __init__(self):
        super(YellowState, self).__init__()
        self.color = f'{clr[2]}Yellow{clr[3]}'
        self.c = 'y'
        logger.info("YellowState created")
