import logging
import time

from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import connector

logger = logging.getLogger(__name__)
longpress_time = 0.3


class GPIOManager():

    def __init__(self, frontend, pins):

        self.frontend = frontend
        self.correctlyLoaded = False

        # Play Led
        self.led_pin = pins['pin_play_led']

        try:
            # GPIO Mode
            gpio.init()
            gpio.setcfg(port.PA10, gpio.OUTPUT)
            # GPIO.setup(self.led_pin, GPIO.OUT)
            self.correctlyLoaded = True

        except RuntimeError:
            logger.error("TTSGPIO-OPI: Not enough permission " +
                         "to use GPIO. GPIO input will not work")

    def set_led(self, led_state):
        if self.correctlyLoaded:
            gpio.output(port.PA10, led_state)
            # GPIO.output(self.led_pin, led_state)
    
