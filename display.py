#import LCD Driver (installed on Pi)
import drivers

from time import sleep

display = drivers.Lcd()

for x in range(10):
    try:
        display.lcd_display_string("I work", 1)  # Write line of text to first line of display
        display.lcd_display_string("yay!", 2)  # Write line of text to second line of display
        sleep(1)                                           # Give time for the message to be read
        display.lcd_clear()                                # Clear the display of any data
        sleep(1)                                           # Give time for the message to be read
    except:
        print("error in except")
        display.lcd_clear()
display.lcd_clear()
