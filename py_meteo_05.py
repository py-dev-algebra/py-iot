# Napisati aplikaciju koja ovisno o postotku vlaznosti zraka, 
# LED matricu puni pixel po pixel, bojom po izboru.
# Kada je vlaznost zraka 0% matrica je prazna (crna),
# a kada je 100% onda je puna (boja po izboru)

from sense_emu import SenseHat
import time


def get_led_matrix_picture(color_up, color_down, humidity):
    led_matrix = []
    
    for i in range(64):
        if i < int(round(64/100, 2) * humidity):
            led_matrix.append(color_up)
        else:
            led_matrix.append(color_down)

    return led_matrix



hat = SenseHat()
hat.clear()

black = [0, 0, 0]
white = [255, 255, 255]

while True:
    humidity = round(hat.get_humidity(), 2)
    led_matrix = get_led_matrix_picture(white, black, humidity)

    hat.set_pixels(led_matrix)
    time.sleep(1)


# Verzija kolegice Nikoline
# while True:
#     air_humidity = round(hat.get_humidity(), 2)
#     matrix_humidity = int(air_humidity / 100 * 64)
#     pixels = []
#     for i in range(64):
#         if i < matrix_humidity:
#             pixels.append([0, 255, 0])
#         else:
#             pixels.append([0, 0, 0])
#     hat.set_pixels(pixels) 