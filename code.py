# When button pressed: send F10, then one of F1-F8.

import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from digitalio import DigitalInOut, Direction, Pull

# Set up a keyboard device.
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

# Setup the buttons with internal pull-down resistors
buttons = []
for pin in [board.D2, board.D3, board.D4, board.D5, board.D6, board.D7, board.D8, board.D9]: # kb2040 pins
    button = DigitalInOut(pin)
    button.direction = Direction.INPUT
    button.pull = Pull.DOWN
    buttons.append(button)

# Each button corresponds to a key or key combination or a sequence of keys
keys = [
    Keycode.F1,
    Keycode.F2,
    Keycode.F3,
    Keycode.F4,
    Keycode.F5,
    Keycode.F6,
    Keycode.F7,
    Keycode.F8,
  
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

while True:
    # check each button
    for button, key in zip(buttons, keys):
        if button.value:  # button is pressed
            kbd.press(Keycode.F10)
            time.sleep(0.01)
            kbd.press(key)
            kbd.release_all()
            time.sleep(0.1)  # debounce delay
    time.sleep(0.1)
