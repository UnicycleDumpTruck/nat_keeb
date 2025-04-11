/* Released into the public domain */
/* Earle F. Philhower, III <earlephilhower@yahoo.com> */

#include <Keyboard.h>
#include <Debounce.h>

#define NUM_PINS 8
const uint8_t BUTTON_PINS[] = {2,3,4,5,6,7,8,9};
const uint8_t NUM_BUTTONS = sizeof(BUTTON_PINS) / sizeof(BUTTON_PINS[0]);
const uint8_t INTERVAL_DEBOUNCE = 1;       // Update button state every 1ms
uint32_t timeDebounce = 0;                 // Time of last debounce update

Debounce* buttons[NUM_BUTTONS];            // Array of button objects

void ledCB(bool numlock, bool capslock, bool scrolllock, bool compose, bool kana, void *cbData) {
  (void) numlock;
  (void) scrolllock;
  (void) compose;
  (void) kana;
  (void) cbData;
  digitalWrite(LED_BUILTIN, capslock ? HIGH : LOW);
}

void setup() {
  Serial.begin(115200);
  delay(5000);

  // Initialize buttons and LEDs
  for (uint8_t i = 0; i < NUM_BUTTONS; i++)
  {
      buttons[i] = new Debounce(BUTTON_PINS[i], LOW); // Create button object
      pinMode(BUTTON_PINS[i], INPUT_PULLUP);    // Set button pin as input
            
      Serial.print("Button ");
      Serial.print(i);
      Serial.print(" on pin ");
      Serial.print(BUTTON_PINS[i]);
  }

  Keyboard.onLED(ledCB);
  Keyboard.begin();
  Serial.println("News Around Town Green Screen waiting for buttons:");
}

void sendKeyPress(int key) {
  switch (key) {
    case 0:
      Keyboard.write('1');
      break;
    case 1:
      Keyboard.write('2');
      break;
    case 2:
      Keyboard.write('3');
      break;
    case 3:
      Keyboard.write('4');
      break;
    case 4:
      Keyboard.write('5');
      break;
    case 5:
      Keyboard.write('6');
      break;
    case 6:
      Keyboard.write('7');
      break;
    case 7:
      Keyboard.write('8');
      break;
    default:
      break;

  }
}

void loop() {
  uint32_t currentMillis = millis();
  // Non-interrupt approach: update button state at regular intervals
  if (currentMillis - timeDebounce >= INTERVAL_DEBOUNCE)
  {
      timeDebounce = currentMillis;
      
      // Update all buttons
      for (uint8_t i = 0; i < NUM_BUTTONS; i++)
      {
          buttons[i]->update();          // Update button state every 1ms
      }
  }
  
  // Check all buttons for events and update LEDs
  for (uint8_t i = 0; i < NUM_BUTTONS; i++)
  {
      if (buttons[i]->isPressed())
      {
          // Toggle corresponding LED
          Serial.print("Button ");
          Serial.print(i);
          Serial.println(" pressed");
          sendKeyPress(i);
      }
  }

}
