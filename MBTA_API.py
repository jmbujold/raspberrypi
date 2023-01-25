# import urllib library, used to access the API URL
from urllib.request import urlopen
import requests

# import json library to parse JSON response from API
import json 

# using datetime module, used to get current time
from datetime import datetime
from datetime import timezone
 
 
# ct stores current time, ISO format seemed to match the MBTA time (looks like '2023-01-25T11:51:01')
ct = datetime.now().replace(microsecond=0).isoformat()


# store MBTA API that returns JSON with train information for place-ccmnl stop - inbound (Community College, Orange Line, Inbound)
url = "https://api-v3.mbta.com/predictions?filter[stop]=place-ccmnl&filter[direction_id]=0"
  
# store the response of URL
response = urlopen(url)

#load JSON to variable, then get first train (0) and second train (1) arrival times. Time looks like '2023-01-25T11:57:00-05:00'
data_json = json.loads(response.read())
first_train = data_json['data'][0]['attributes']['arrival_time']
second_train = data_json['data'][1]['attributes']['arrival_time']


#function to take two timestamps in string format and return the difference between them as INT. First time should be in the future, second should be current/earlier
def difference(first,second):
    day1 = first[8:10] #parse our the two digit day
    day2 = second[8:10]
    day_diff = int(day1) - int(day2)
    hour1 = first[11:13] #parse our the two digit hour
    hour2 = second[11:13]
    hour_diff = int(hour1) - int(hour2)
    min1 = first[14:16] #parse our the two digit difference
    min2 = second[14:16]
    min_diff = int(min1) - int(min2)
    total_diff = (1140*day_diff) + (60*hour_diff) + min_diff #find the minute difference if days/hours are different
    if (total_diff == 0):
            total_diff = "Now" #if arriving train is same as current time, display now
    return total_diff


print("Community College Inbound:")
print("Next Train: ", difference(first_train,ct), " Min")
print("---")
print("Community College Inbound")
print("Fol. Train: ", difference(second_train,ct), " Min")

