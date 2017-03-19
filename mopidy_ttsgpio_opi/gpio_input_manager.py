import logging
import time
import subprocess

logger = logging.getLogger(__name__)
longpress_time = 0.3

class GPIOManager():

    def __init__(self, frontend, pins):

        self.frontend = frontend
        self.correctlyLoaded = False

        # Play Led
        self.led_pin = pins['pin_play_led']
        self.inverted = pins['inverted']

        try:
            self.correctlyLoaded = True

        except RuntimeError:
            logger.error("TTSGPIO-OPI: Not enough permission " +
                         "to use GPIO. GPIO input will not work")

    def set_led(self, led_state):
        if self.correctlyLoaded:
            if led_state == 0 if self.inverted else 1:
                subprocess.Popen('echo 1 > /sys/class/gpio_sw/' + self.led_pin + '/data', shell=True)
            else:
                subprocess.Popen('echo 0 > /sys/class/gpio_sw/' + self.led_pin + '/data', shell=True)
