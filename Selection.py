import sqlite3
import re
from Event import update_event_active_status


def validate_selection(_name, _event, _price, _active, _outcome):

    name, event, price, active, outcome = None, None, None, None, None

    name = _name if _name else print('Invalid name for selection')
    event = _event if _event else print('Invalid event for selection')
    price = _price if re.match(r'[0-9]*\.[0-9]{2}', _price) else\
        print('Invalid format for price. Accepted format is numeric with 2 decimal places')

    active = _active if _active in ('True', 'true', 'False', 'false') else\
        print('Allowed values for active are "True/true or False/false"')

    outcome = _outcome if _outcome in ('unsettled', 'void', 'lose', 'win') else\
        print('Invalid value for outcome. Allowed values are "unsettled, void , lose, win"')

    data_tuple = (name, event, price, active, outcome)

    return data_tuple


def create_selection(_name, _event, _price, _active, _outcome):

    data_tuple = validate_selection(_name, _event, _price, _active, _outcome)

    if all(data_tuple):

        sql = 'INSERT INTO selection VALUES (?,?,?,?,?);'
        conn = sqlite3.connect('database/sportsbook.db')
        cur = conn.cursor()

        try:
            cur.execute(sql, data_tuple)
        except sqlite3.IntegrityError:
            print('Duplicate value in name for events.name')

        conn.commit()
        conn.close()


def read_selection():

    conn = sqlite3.connect('database/sportsbook.db')

    cur = conn.cursor()
    sql = 'select * from selection'
    cur.execute(sql)
    rows = cur.fetchall()

    conn.close()

    print('--- Selections ---')
    print(' Name | Event | Price | Active | Outcome')

    for row in rows:
        print(row)

    print('-----------------')


def update_selection_outcome(_name, _outcome):

    invalid_input = False

    name = _name

    if _outcome in ('unsettled', 'void', 'lose', 'win'):
        outcome = _outcome
    else:
        print('Invalid Input for status. Allowed values are "unsettled, void, lose, win"')
        invalid_input = True

    if not invalid_input:

        conn = sqlite3.connect('database/sportsbook.db')
        cur = conn.cursor()
        cur.execute('UPDATE selection '
                    'SET outcome = ?'
                    'where selection_name = ?', (outcome, name))

        conn.commit()
        conn.close()


def update_selection_active_status(_name, _active_status):

    invalid_input = False

    name = _name

    if _active_status in ('true', 'True', 'False', 'false'):
        active_status = _active_status
    else:
        print('Invalid Input for active status. Allowed values are "true, True, False, false"')
        invalid_input = True

    if not invalid_input:
        conn = sqlite3.connect('database/sportsbook.db')
        cur = conn.cursor()
        cur.execute('UPDATE selection '
                    'SET active = ?'
                    'where selection_name = ?', (active_status, name))

        conn.commit()
        conn.close()







