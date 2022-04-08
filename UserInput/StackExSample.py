from evdev import list_devices, InputDevice, categorize, ecodes

CENTER_TOLERANCE = 350
STICK_MAX = 65536

dev = InputDevice( list_devices()[0] )
axis = {
    ecodes.ABS_X: 'ls_x', # 0 - 65,536   the middle is 32768
    ecodes.ABS_Y: 'ls_y',
    ecodes.ABS_Z: 'rs_x',
    ecodes.ABS_RZ: 'rs_y',
    ecodes.ABS_BRAKE: 'lt', # 0 - 1023
    ecodes.ABS_GAS: 'rt',

    ecodes.ABS_HAT0X: 'dpad_x', # -1 - 1
    ecodes.ABS_HAT0Y: 'dpad_y'
}

center = {
    'ls_x': STICK_MAX/2,
    'ls_y': STICK_MAX/2,
    'rs_x': STICK_MAX/2,
    'rs_y': STICK_MAX/2
}

last = {
    'ls_x': STICK_MAX/2,
    'ls_y': STICK_MAX/2,
    'rs_x': STICK_MAX/2,
    'rs_y': STICK_MAX/2
}

for event in dev.read_loop():

    # calibrate zero on Y button
    if event.type == ecodes.EV_KEY:
        if categorize(event).keycode[0] == "BTN_WEST":
            center['ls_x'] = last['ls_x']
            center['ls_y'] = last['ls_y']
            center['rs_x'] = last['rs_x']
            center['rs_y'] = last['rs_y']
            print( 'calibrated' )

    #read stick axis movement
    elif event.type == ecodes.EV_ABS:
        if axis[ event.code ] in [ 'ls_x', 'ls_y', 'rs_x', 'rs_y' ]:
            last[ axis[ event.code ] ] = event.value

            value = event.value - center[ axis[ event.code ] ]

            if abs( value ) <= CENTER_TOLERANCE:
                value = 0

            if axis[ event.code ] == 'rs_x':
                if value < 0:
                    print('left')
                else:
                    print('right')
                print( value )

            elif axis[ event.code ] == 'ls_y':
                if value < 0:
                    print('foreward')
                else:
                    print('backward')
                print( value )