from evdev import list_devices, InputDevice, categorize, ecodes, KeyEvent

CENTER_TOLERANCE = 1000
STICK_MAX = 65536

dev = InputDevice( list_devices()[1] )
last = {"ABS_X": STICK_MAX/2, "ABS_Y": STICK_MAX/2}

for event in dev.read_loop():
    if event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        if absevent.event.type == 0:
            continue
        try:
            
            if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_Y':
                last["ABS_Y"] = absevent.event.value
                
            elif ecodes.bytype[absevent.event.value][absevent.event.code] == 'ABS_X':
                last["ABS_X"] = absevent.event.value
            else:
                continue
            
        except KeyError:
            print("Key Error")
        
        if last["ABS_X"] < -STICK_MAX/4:
            print("reverse")
        if last["ABS_X"] > STICK_MAX/4:
            print("forward")
            
        if last["ABS_Y"] > STICK_MAX/4:
            print("left")
        if last["ABS_Y"] < -STICK_MAX/4:
            print("right")
            
        print("__________")
