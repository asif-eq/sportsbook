from Sport import *
from Event import *
from Selection import *


check_event_active_status('ireland vs germany football match')
check_sports_active_status('football')
update_selection_outcome('ireland to win ireland vs germany football match', 'lose')
update_selection_outcome('germany to win ireland vs germany football match', 'win')
update_selection_active_status('ireland to win ireland vs germany football match', 'false')
update_selection_active_status('germany to win ireland vs germany football match', 'false')
read_selection()
check_event_active_status('ireland vs england germany match')


check_sports_active_status('football')
read_sports()