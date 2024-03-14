from sense_emu import SenseHat


hat = SenseHat()
hat.clear()


def display_pixel(x, y):
    hat.set_pixel(x, y, [0, 255, 0])


def move_dot(event):
    global x, y

    if event.direction == 'up':
        display_pixel(x, y - 1)
    elif event.direction == 'down':
        display_pixel(x, y + 1)
    elif event.direction == 'left':
        display_pixel(x - 1, y)
    elif event.direction == 'right':
        display_pixel(x + 1, y)


x = int(input('Unesite pocetnu x koordinatu pixela:'))
y = int(input('Unesite pocetnu y koordinatu pixela:'))
start_position = display_pixel(x, y)

while True:
    joystick_events = hat.stick.get_events()

    for event in joystick_events:
        if event.action == 'released' and event.direction == 'up':
            move_dot(event)
        elif event.action == 'released' and event.direction == 'down':
            move_dot(event)
        elif event.action == 'released' and event.direction == 'left':
            move_dot(event)
        elif event.action == 'released' and event.direction == 'right':
            move_dot(event)
