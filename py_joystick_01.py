from sense_emu import SenseHat


hat = SenseHat()
hat.clear()


def move_dot():
    pass


while True:
    joystick_events = hat.stick.get_events()

    for event in joystick_events:
        if event.action == 'released' and event.direction == 'up':
            # print('Pokreni funkciju koja pomice OBJEKT prema gore')
            move_dot()
        elif event.action == 'released' and event.direction == 'down':
            # print('Pokreni funkciju koja pomice OBJEKT prema dolje')
            move_dot()
        elif event.action == 'released' and event.direction == 'left':
            # print('Pokreni funkciju koja pomice OBJEKT prema lijevo')
            move_dot()
        elif event.action == 'released' and event.direction == 'right':
            # print('Pokreni funkciju koja pomice OBJEKT prema desno')
            move_dot()
        elif event.action == 'released' and event.direction == 'middle':
            # print('Pokreni funkciju koja reagira na tipku ENTER')
            move_dot()
