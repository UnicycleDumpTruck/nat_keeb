# When button pressed: send F10, then one of F1-F8.

import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
#from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from digitalio import DigitalInOut, Direction, Pull
from adafruit_debouncer import Debouncer

# Set up a keyboard device.
kbd = Keyboard(usb_hid.devices)
#layout = KeyboardLayoutUS(kbd)

# Setup the buttons with internal pull-down resistors
buttons = []
debouncers = []
for pin in [board.D2, board.D3, board.D4, board.D5, board.D6, board.D7, board.D8, board.D9]: # kb2040 pins
    button = DigitalInOut(pin)
    button.direction = Direction.INPUT
    button.pull = Pull.UP
    buttons.append(button)
    debouncers.append(Debouncer(button))

# Each button corresponds to a key or key combination or a sequence of keys
keys = [
    Keycode.ONE,
    Keycode.TWO,
    Keycode.THREE,
    Keycode.FOUR,
    Keycode.FIVE,
    Keycode.SIX,
    Keycode.SEVEN,
    Keycode.EIGHT,
  
    # Keycode.A,
    # (Keycode.COMMAND, Keycode.TAB),
    # [
    #     Keycode.UP_ARROW,
    #     Keycode.ENTER
    # ],
    # [
    #     Keycode.END,
    #     (Keycode.SHIFT, Keycode.HOME),
    #     (Keycode.COMMAND, Keycode.C),
    # ],
    # [
    #     (Keycode.CONTROL, Keycode.A),
    #     'Hello World',
    #     Keycode.PERIOD
    # ]
]
print("Setup complete, starting loop")
while True:
    # check each button
#    for button, key in zip(buttons, keys):
#        if button.value:  # button is pressed
#            kbd.press(Keycode.F10)
#            time.sleep(0.01)
#            kbd.press(key)
#            kbd.release_all()
#            time.sleep(0.1)  # debounce delay
    for debouncer, key in zip(debouncers, keys):
        debouncer.update()
        if debouncer.fell:
            #kbd.send(Keycode.F10)
#            kbd.release_all()
            kbd.send(key)
#            kbd.release_all()
            print(key,time.monotonic())
            time.sleep(0.01)
#            kbd.press(key)
#            kbd.release_all()
#            time.sleep(0.05)
#            kbd.press(key)
            #kbd.release(Keycode.F10)
#            time.sleep(0.01)
            #kbd.send(key)
#    time.sleep(0.1)
