#This function is for translating a matrix (how you see the board)
# to the LED input on a raspberry pi. FastLED addresses LEDs in a line 
# so we need to convert matrix to a single line. 


import time
from rpi_ws281x import Color, PixelStrip, ws

LED_COUNT = 144        
LED_PIN = 18           # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000   # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10           # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255   # Set to 0 for darkest and 255 for brightest
LED_INVERT = False     # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0


# A Class is likely unneccessary here as this is fairly 
# low level and should have very little overhead so that we can update
# the board in as close to real time as possible
def DisplayColorMatrix(matrix):

    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
    
    
    y = 6
    x = 0

    for i in range(LED_COUNT):
        #if type(matrix[y][x]) != type(Color(0,0,0)):
        #    raise TypeError ("The matrix should only contain Color types")
        #else:
        strip.setPixelColor(i, matrix[y][x])

        if x % 2 == 0:
            y = y + 1
        else:
            y = y - 1

        if y == 5 and i < 71:
            y = 6
            x = x + 1
        if y == 12 and i < 71:
            y = 11
            x = x + 1
        if y == -1 and i > 72:
            y = 0
            x = x - 1
        if y == 6 and i > 72:
            y = 5
            x = x - 1
    
    strip.show()

    