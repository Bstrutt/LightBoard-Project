import sys
import sdl2
import sdl2.ext

sdl2.ext.init()

while(True):
    events = sdl2.ext.get_events()
    for even in events:
        print(even)
        if event.type == sdl2.SDL_QUIT:
            quit()