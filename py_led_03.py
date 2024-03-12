from sense_emu import SenseHat
import time

hat = SenseHat()

hat.clear()
hat.set_pixel(0, 2, [0, 255, 0])
hat.set_pixel(0, 1, [255, 0, 0])
