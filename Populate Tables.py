import csv
from Sport import create_sports
from Event import create_event
from Selection import create_selection

# open the sports.csv file from inputs. Read lines one by one. Create new entries for
with open('inputs/sports.csv', 'r') as sports_file:
    lines = csv.reader(sports_file)
    for line in lines:
        create_sports(*line)
sports_file.close()


with open('inputs/events.csv', 'r') as events_file:
    lines = csv.reader(events_file)
    for line in lines:
        create_event(*line)
events_file.close()


with open('inputs/selection.csv', 'r') as selection_file:
    lines = csv.reader(selection_file)
    for line in lines:
        create_selection(*line)
selection_file.close()
