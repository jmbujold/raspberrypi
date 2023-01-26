# import urllib library, used to access the API URL
from urllib.request import urlopen

# import json library to parse JSON response from API
import json 

#import LCD Driver (installed on Pi)
import drivers

# using datetime module, used to get current time
from datetime import datetime, timezone, timedelta
from dateutil.parser import parse
from time import sleep

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = drivers.Lcd()
 
# ct stores current time, ISO format seemed to match the MBTA time (looks like '2023-01-25T11:51:01')
ct = parse(datetime.now().replace(microsecond=0).isoformat())


# store MBTA API that returns JSON with train information for place-ccmnl stop - inbound (Community College, Orange Line, Inbound)
url = "https://api-v3.mbta.com/predictions?filter[stop]=place-ccmnl&filter[direction_id]=0"
  
# store the response of URL
response = urlopen(url)
print("response",response)
print(type(response))

#load JSON to variable, then get first train (0) and second train (1) arrival times. Time looks like '2023-01-25T11:57:00-05:00'
data_json = json.loads(response.read())

#load JSON to variable, then get first train (0) and second train (1) arrival times. Time looks like '2023-01-25T11:57:00-05:00'
first_train = parse(data_json['data'][0]['attributes']['arrival_time']).replace(tzinfo=None)
second_train = parse(data_json['data'][1]['attributes']['arrival_time']).replace(tzinfo=None)


print("Community College Inbound:")
print("Next Train: ", first_train - ct, " Min")
print("---")
print("Community College Inbound")
print("Fol. Train: ", second_train - ct, " Min")

# Main body of code
try:
    while True:
        # Remember that your sentences can only be 16 characters long!
        print("Writing to display")
        display.lcd_display_string("Comm Col Inbound", 1)  # Write line of text to first line of display
        display.lcd_display_string(str(first_train - ct)), 2)  # Write line of text to second line of display
        sleep(2)                                           # Give time for the message to be read
        display.lcd_clear()                                # Clear the display of any data
        sleep(1)                                           # Give time for the message to be read
        display.lcd_display_string("Comm Col Inbound", 1)  # Write line of text to first line of display
        display.lcd_display_string(str(second_train - ct)), 2)  # Write line of text to second line of display
        sleep(2)                                           # Give time for the message to be read
        display.lcd_clear()                                # Clear the display of any data
        sleep(1)                                           # Give time for the message to be read
except KeyboardInterrupt:
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
