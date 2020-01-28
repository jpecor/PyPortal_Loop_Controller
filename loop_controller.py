
"""
`loop_controller`
================================================================================
This is a simple prototype control interface for a looper sequence.  It is 
designed to control GarageBand via USB HID keycode commands.  

The control is crude. It used the UP/DOWN arrrow keycode and "M" to mute/unmute 
channels. However, there are not many options for controlling GarageBand tracks
so this works.

* Author: Jason Pecor

"""
import board
import time
import adafruit_touchscreen
from adafruit_pyportal import PyPortal

from adafruit_bitmap_font import bitmap_font
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from padded_button import PaddedButton

# Enable/disable sending the keycodes.  This will help prevent surprise syntax errors
# in the code when testing the touchscreen.  :)
send_codes = True

# Colors
WHITE = 0xffffff
BLUE = 0x094A85
LIGHT_BLUE = 0x13BDF9
DARK_BLUE = 0x0D2035
LIGHT_GREEN = 0x009A6E
GREEN = 0x45E83A
ORANGE = 0xDF550F
RED = 0xDB1308
GREY = 0x3B3C3E
BLACK = 0x000000

# The buttons on the TFT display will send keycodes just like a standard keyboard
keyboard = Keyboard()
keyboard_layout = KeyboardLayoutUS(keyboard)

# Some GarageBand/Song specific definitions
max_tracks = 12

# Setup touchscreen
# ts = adafruit_touchscreen.Touchscreen(board.TOUCH_XL, board.TOUCH_XR,
#                                       board.TOUCH_YD, board.TOUCH_YU,
#                                       calibration=((5200, 59000), (5800, 57000)),
#                                       size=(320, 240), z_threshhold=5000)

ts = adafruit_touchscreen.Touchscreen(board.TOUCH_XL, board.TOUCH_XR,
                                      board.TOUCH_YD, board.TOUCH_YU,
                                      size=(320, 240))

# Load the font to be used on the buttons
font = bitmap_font.load_font("/fonts/Dina.bdf")

# As it turns out, the code above can all be replaced with the following:
pyportal = PyPortal(default_bg=0x000000)

button_margin = (1,1)
button_height = 80
button_width = 80

btn_0_0 = PaddedButton(x=0, y=0, width=button_width, height=button_height, label="T-1-1",
                            label_font=font, label_color=0xffffFF,
                            fill_color=0x094A85, outline_color=0x094A85,
                            selected_fill=0x00ff00, selected_outline=0x094A85, style=1,
                            margin=button_margin, padding=(5, 5))

btn_0_1 = PaddedButton(x=80, y=0, width=button_width, height=button_height, label="T-1-2",
                            label_font=font, label_color=0xffffFF,
                            fill_color=0x094A85, outline_color=0x094A85,
                            selected_fill=0x00ff00, selected_outline=0x094A85, style=1,
                            margin=button_margin, padding=(5, 5))

btn_0_2 = PaddedButton(x=160, y=0, width=button_width, height=button_height, label="T-1-3",
                            label_font=font, label_color=0xffffFF,
                            fill_color=0x094A85, outline_color=0x094A85,
                            selected_fill=0x00ff00, selected_outline=0x094A85, style=1,
                            margin=button_margin, padding=(5, 5))

btn_0_3 = PaddedButton(x=240, y=0, width=button_width, height=button_height, label="T-1-4",
                            label_font=font, label_color=0xffffFF,
                            fill_color=0x094A85, outline_color=0x094A85,
                            selected_fill=0x00ff00, selected_outline=0x094A85, style=1,
                            margin=button_margin, padding=(5, 5))

btn_1_0 = PaddedButton(x=0, y=80, width=button_width, height=button_height, label="T-2-1",
                            label_font=font, label_color=0xffffFF,
                            fill_color=0xC10721, outline_color=0xC10721,
                            selected_fill=0x00ff00, selected_outline=0xC10721, style=1,
                            margin=button_margin, padding=(5, 5))

btn_1_1 = PaddedButton(x=80, y=80, width=button_width, height=button_height, label="T-2-2",
                            label_font=font, label_color=0xffffFF,
                            fill_color=0xC10721, outline_color=0xC10721,
                            selected_fill=0x00ff00, selected_outline=0xC10721, style=1,
                            margin=button_margin, padding=(5, 5))

btn_1_2 = PaddedButton(x=160, y=80, width=button_width, height=button_height, label="T-2-3",
                            label_font=font, label_color=0xffffFF,
                            fill_color=0xC10721, outline_color=0xC10721,
                            selected_fill=0x00ff00, selected_outline=0xC10721, style=1,
                            margin=button_margin, padding=(5, 5))

btn_1_3 = PaddedButton(x=240, y=80, width=button_width, height=button_height, label="T-2-4",
                            label_font=font, label_color=0xffffFF,
                            fill_color=0xC10721, outline_color=0xC10721,
                            selected_fill=0x00ff00, selected_outline=0xC10721, style=1,
                            margin=button_margin, padding=(5, 5))

btn_2_0 = PaddedButton(x=0, y=160, width=button_width, height=button_height, label="T-3-1",
                            label_font=font, label_color=0xffffFF,
                            fill_color=ORANGE, outline_color=ORANGE,
                            selected_fill=0x00ff00, selected_outline=ORANGE, style=1,
                            margin=button_margin, padding=(5, 5))

btn_2_1 = PaddedButton(x=80, y=160, width=button_width, height=button_height, label="T-3-2",
                            label_font=font, label_color=0xffffFF,
                            fill_color=ORANGE, outline_color=ORANGE,
                            selected_fill=0x00ff00, selected_outline=ORANGE, style=1,
                            margin=button_margin, padding=(5, 5))

btn_2_2 = PaddedButton(x=160, y=160, width=button_width, height=button_height, label="T-3-3",
                            label_font=font, label_color=0xffffFF,
                            fill_color=ORANGE, outline_color=ORANGE,
                            selected_fill=0x00ff00, selected_outline=ORANGE, style=1,
                            margin=button_margin, padding=(5, 5))

btn_2_3 = PaddedButton(x=240, y=160, width=button_width, height=button_height, label="T-3-4",
                            label_font=font, label_color=0xffffFF,
                            fill_color=ORANGE, outline_color=ORANGE,
                            selected_fill=0x00ff00, selected_outline=ORANGE, style=1,
                            margin=button_margin, padding=(5, 5))

# Add all of the buttons to a list
buttons = [btn_0_0,
           btn_0_1,
           btn_0_2,
           btn_0_3,
           btn_1_0,
           btn_1_1,
           btn_1_2,
           btn_1_3,
           btn_2_0,
           btn_2_1,
           btn_2_2,
           btn_2_3
           ]

# Add margin and padding to all of the buttons
# And add to the display
for button in buttons:
    pyportal.splash.append(button.group)
    button.selected = False

last_touchpoint = None  # Will be used to trap Off->On touch transition


def trigger_track(track):
    # Send down arrow keycodes to desired track and mute/unmute
    for track in range(track-1):
        keyboard.send(Keycode.DOWN_ARROW)
    keyboard.send(Keycode.M)

# Main code loop
while True:

    touchpoint = ts.touch_point  # Grab a touch point if one happens

    if (touchpoint is not None) & (last_touchpoint is None):  # Only catch the Off->On transition

        (y, x, z) = touchpoint

        for i, b in enumerate(buttons):
            
            if b.contains(touchpoint):
 
                b.selected = not b.selected

                print("Button {} pressed.".format(b.label))

                if send_codes:
                    if b == btn_0_0:
                        trigger_track(1)
                    elif b == btn_0_1:
                        trigger_track(2)
                    elif b == btn_0_2:
                        trigger_track(3)
                    elif b == btn_0_3:
                        trigger_track(4)
                    elif b == btn_1_0:
                        trigger_track(5)
                    elif b == btn_1_1:
                        trigger_track(6)
                    elif b == btn_1_2:
                        trigger_track(7)
                    elif b == btn_1_3:
                        trigger_track(8)
                    elif b == btn_2_0:
                        trigger_track(9)
                    elif b == btn_2_1:
                        trigger_track(10)
                    elif b == btn_2_2:
                        trigger_track(11)
                    elif b == btn_2_3:
                        trigger_track(12)

        # Return to top of tracks (Crude but it works)
        for track in range(max_tracks-1):
            keyboard.send(Keycode.UP_ARROW) 

    # Capture state of p to setup one-shot compare
    time.sleep(0.25)
    last_touchpoint = touchpoint
