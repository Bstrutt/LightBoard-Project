#include <FastLED.h>

#define LED_PIN     7
#define NUM_LEDS    150
#define BRIGHTNESS  127
#define LED_TYPE    WS2811
#define COLOR_ORDER RGB
CRGB leds[NUM_LEDS];

#define UPDATES_PER_SECOND 100

void setup() {
    
  FastLED.addLeds<LED_TYPE, LED_PIN, COLOR_ORDER>(leds, NUM_LEDS).setCorrection(TypicalLEDStrip);
  FastLED.setBrightness(BRIGHTNESS); 
}

void loop() {
  int WALL_LEDS = 144;
  for (int i = 0; i < WALL_LEDS; i++){
    int STRING_LENGTH = 5;
    for (int l = 0; l < STRING_LENGTH; l++){
      leds[(i+l) % WALL_LEDS].red = 0;
      leds[(i+l) % WALL_LEDS].blue = 127;
      leds[(i+l) % WALL_LEDS].green = 0;
    }
    
    for (int j = 0; j < WALL_LEDS; j++){
      if (j < i || j > i + STRING_LENGTH % WALL_LEDS){
        leds[j].red = 0;
        leds[j].blue = 0;
        leds[j].green = 0;
      }
    }
    delay(50);
    FastLED.show();
  }
  
}
