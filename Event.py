import sqlite3
from Sport import update_sport_active_status


def validate_event(_name, _slug, _active, _type, _sport, _status, _scheduled_start, _actual_start):

    """ This function performs basic validations of the inputs that is to be entered into the system
    For e.g. check if the name field (Primary key) is not empty."""

    name, slug, active, type_, status = None, None, None, None, None

    name = _name if _name else print('Name cannot be empty')
    slug = _slug if _slug else print('Slug cannot be empty')
    active = _active if _active in ('True', 'true', 'False', 'false') else\
        print('Allowed values for slug are "True/true or False/false"')
    type_ = _type if _type in ('preplay', 'inplay') else\
        print('Allowed values for type are "preplay or inplay"')
    status = _status if _status in ('pending', 'started', 'ended', 'cancelled') else\
        print('Allowed values for status are "pending, started, ended, cancelled"')

    data_tuple = (name, slug, active, type_, _sport, status, _scheduled_start, _actual_start)

    return data_tuple


def create_event(_name, _slug, _active, _type, _sport, _status, _scheduled_start, _actual_start):

    """This function takes the validated input and creates a new row entry for events table"""

    data_tuple = validate_event(_name, _slug, _active, _type, _sport, _status, _scheduled_start, _actual_start)

    # Insert into the database only if all the values are validated. If any value is None
    # then the row will not be entered into the database

    if all(data_tuple):

        sql = 'INSERT INTO event VALUES (?,?,?,?,?,?,?,?)'
        conn = sqlite3.connect('database/sportsbook.db')
        cur = conn.cursor()

        # check if an entry for name already exists
        try:
            cur.execute(sql, data_tuple)
        except sqlite3.IntegrityError:
            print('Duplicate value in name for events.name')

        conn.commit()
        conn.close()


def read_event():

    """This function reads the event table and prints them on console"""

    conn = sqlite3.connect('database/sportsbook.db')

    cur = conn.cursor()
    sql = 'select * from event'
    cur.execute(sql)

    rows = cur.fetchall()

    conn.close()

    print('--- Events ---')
    print('Name | Slug | Active | Type | Sport | Status | Scheduled Start | Actual Start')

    for row in rows:
        print(row)

    print('----------------------')


def update_event_status(_name, _status):

    invalid_input = False

    name = _name

    if _status in ('pending', 'started', 'ended', 'cancelled'):
        status = _status
    else:
        print('Invalid Input for status. Allowed values are "pending, started, ended, cancelled"')
        invalid_input = True

    if not invalid_input:
        conn = sqlite3.connect('database/sportsbook.db')
        cur = conn.cursor()

        cur.execute('UPDATE event '
                    'SET status = ?'
                    'where event_name = ?', (status, name))

        conn.commit()
        conn.close()


def check_event_active_status(name):

    conn = sqlite3.connect('database/sportsbook.db')

    # select a list of rows instead a list of tuples so that values can be compared
    conn.row_factory = lambda cursor, row: row[0]
    cur = conn.cursor()
    rows = cur.execute("select active from selection where event = ?", (name,)).fetchall()

    if 'true' in rows or 'True' in rows:
        print(f'The event {name} is still active')

    # if all selections are inactive make the event inactive
    else:
        update_event_active_status(name, 'false')
        print(f'The event {name} is now inactive')


def update_event_active_status(_name, _active_status):

    invalid_input = False

    name = _name

    if _active_status in ('True', 'true', 'False', 'false'):
        active_status = _active_status
    else:
        print('Invalid Input for status. Allowed values are "pending, started, ended, cancelled"')
        invalid_input = True

    if not invalid_input:
        conn = sqlite3.connect('database/sportsbook.db')
        cur = conn.cursor()

        cur.execute('UPDATE event '
                    'SET active = ?'
                    'where event_name = ?', (active_status, name))

        conn.commit()
        conn.close()





