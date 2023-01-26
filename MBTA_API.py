# import urllib library, used to access the API URL
from urllib.request import urlopen
import requests

# import json library to parse JSON response from API
import json 

# using datetime module, used to get current time
from datetime import datetime, timezone, timedelta
from dateutil.parser import parse
 
 
# ct stores current time, ISO format seemed to match the MBTA time (looks like '2023-01-25T11:51:01')
ct = parse(datetime.now().replace(microsecond=0).isoformat())


# store MBTA API that returns JSON with train information for place-ccmnl stop - inbound (Community College, Orange Line, Inbound)
url = "https://api-v3.mbta.com/predictions?filter[stop]=place-ccmnl&filter[direction_id]=0"
  
# store the response of URL
response = urlopen(url)

#load JSON to variable, then get first train (0) and second train (1) arrival times. Time looks like '2023-01-25T11:57:00-05:00'
data_json = response.json()

#load JSON to variable, then get first train (0) and second train (1) arrival times. Time looks like '2023-01-25T11:57:00-05:00'
first_train = parse(data_json['data'][0]['attributes']['arrival_time']).replace(tzinfo=None)
second_train = parse(data_json['data'][1]['attributes']['arrival_time']).replace(tzinfo=None)


print("Community College Inbound:")
print("Next Train: ", first_train - ct, " Min")
print("---")
print("Community College Inbound")
print("Fol. Train: ", second_train - ct, " Min")
