#include <Adafruit_NeoPixel.h>
#ifdef AVR
  #include <avr/power.h>
#endif
#define PIN 6
#define NUMPIXELS 8

#define button_left 3 
#define button_right 4

const unsigned long DebounceTime = 10;


boolean ButtonWasPressed = false;
unsigned long ButtonStateChangeTime = 0;

int i;
int button_state1 = 0, button_state2 = 0;

Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);
#define DELAYVAL 500

void setup() {
#if defined(AVR_ATtiny85) && (F_CPU == 16000000)
  clock_prescale_set(clock_div_1);
#endif
  pinMode(button_left, INPUT_PULLUP);
  pinMode(button_right, INPUT_PULLUP);
  pixels.begin();
}

void checkButton1()
{
  unsigned long currentTime = millis();
  boolean buttonIsPressed = digitalRead(button_left) == LOW;  // Active LOW
  if (buttonIsPressed != ButtonWasPressed && currentTime  -  ButtonStateChangeTime > DebounceTime){
    ButtonWasPressed = buttonIsPressed;
    ButtonStateChangeTime = currentTime;
      if (ButtonWasPressed){
        i--;
        pixels.clear();
      }
  }
}

void checkButton2()
{
  unsigned long currentTime = millis();
  boolean buttonIsPressed = digitalRead(button_right) == LOW;  // Active LOW
  if (buttonIsPressed != ButtonWasPressed && currentTime  -  ButtonStateChangeTime > DebounceTime){
    ButtonWasPressed = buttonIsPressed;
    ButtonStateChangeTime = currentTime;
      if (ButtonWasPressed){
        i++;
        pixels.clear();
      }
  }
}
void loop() {
  checkButton1();
  checkButton2();

  pixels.setPixelColor(i, pixels.Color(0, 150, 0));
  pixels.show();
  delay(100);
}
