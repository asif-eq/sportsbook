from Search import *

# search for events featuring Ireland
search_name_having('event', 'ireland')

# search for selections about football
search_name_having('selection', 'football')

# search for events at particular time
event_schedule_time('after', '2021-09-10 09:30:00 ')
# event_schedule_time('at', '2021-09-05 09:30:00')
event_schedule_time('before', '2021-09-20 09:30:00')

