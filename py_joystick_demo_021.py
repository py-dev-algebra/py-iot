from sense_emu import SenseHat


hat = SenseHat()
hat.clear()


def move_dot(event):
    global start_position
    
    if event.action == 'released' and event.direction == 'up':
            #print('Pokreni funkciju koja pomice OBJEKT prema gore')
            start_position = hat.set_pixel(x, y-1, [0, 255, 0])
    elif event.action == 'released' and event.direction == 'down':
            #print('Pokreni funkciju koja pomice OBJEKT prema dolje')
            start_position = hat.set_pixel(x, y+1, [0, 255, 0])
    elif event.action == 'released' and event.direction == 'left':
            #print('Pokreni funkciju koja pomice OBJEKT prema lijevo')
            start_position = hat.set_pixel(x-1,y, [0, 255, 0])
    elif event.action == 'released' and event.direction == 'right':
            #print('Pokreni funkciju koja pomice OBJEKT prema desno')
            start_position = hat.set_pixel(x+1,y, [0, 255, 0])

    
x = int(input('Unesite pocetnu x koordinatu pixela:'))
y = int(input('Unesite pocetnu y koordinatu pixela:'))
start_position = hat.set_pixel(x,y, [0, 255, 0])

while True:
    joystick_events = hat.stick.get_events()

    for event in joystick_events:
        if event.action == 'released' and event.direction == 'up':
            #print('Pokreni funkciju koja pomice OBJEKT prema gore')
            move_dot(event)
        elif event.action == 'released' and event.direction == 'down':
            #print('Pokreni funkciju koja pomice OBJEKT prema dolje')
            move_dot(event)
        elif event.action == 'released' and event.direction == 'left':
            #print('Pokreni funkciju koja pomice OBJEKT prema lijevo')
            move_dot(event)
        elif event.action == 'released' and event.direction == 'right':
            #print('Pokreni funkciju koja pomice OBJEKT prema desno')
            move_dot(event)
        elif event.action == 'released' and event.direction == 'middle':
            #print('Pokreni funkciju koja reagira na tipku ENTER')
            pass
