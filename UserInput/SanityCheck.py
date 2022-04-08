from evdev import list_devices, InputDevice, categorize, ecodes
import time
CENTER_TOLERANCE = 350
STICK_MAX = 65536

dev = InputDevice( list_devices()[1] )
print(dev.name)

for event in dev.read_loop():
    absevent = categorize(event)
    print(str(absevent))
    print(str(absevent.event.type) + "  " + str(absevent.event.code) + "  " + str(absevent.event.value))
    print("____________________")
    time.sleep(1)