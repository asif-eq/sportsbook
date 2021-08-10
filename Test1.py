from Event import *
from Selection import *


# First Set of transactions. After updating the status of both selections for the event 'ireland
# vs england football match' the event should become inactive

check_event_active_status('ireland vs england football match')
update_selection_outcome('ireland to win ireland vs england football match', 'lose')
update_selection_outcome('england to win ireland vs england football match', 'win')
update_selection_active_status('ireland to win ireland vs england football match', 'false')
update_selection_active_status('england to win ireland vs england football match', 'false')
read_selection()
check_event_active_status('ireland vs england football match')