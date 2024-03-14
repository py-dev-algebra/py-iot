from sense_emu import SenseHat

hat = SenseHat()
hat.clear()


x = 0
y = 0
hat.set_pixel(x, y, 0, 255, 0)

def move_dot(direction):
    global x, y
    if direction == 'up':
        if y != 0:
            y = (y - 1) # Tocka miruje
    elif direction == 'down':
        y = (y + 1) % 8 # Ako je % 8 onda se tocka pomoce cirkularno
    elif direction == 'left':
        x = (x - 1) % 8
    elif direction == 'right':
        x = (x + 1) % 8
    hat.clear()
    hat.set_pixel(x, y, 0, 255, 0)


while True:
    joystick_events = hat.stick.get_events()

    for event in joystick_events:
        if event.action == 'released':
            move_dot(event.direction)
