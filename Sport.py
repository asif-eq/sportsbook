import sqlite3


def validate_input(_name, _slug, _active_status):

    name, slug, active_status = None, None, None

    name = _name if _name else print('Name of the sport cannot be empty')
    slug = _slug if _slug else print('Slug of the sport cannot be empty')
    active_status = _active_status if _active_status in ('True', 'true', 'False', 'false') else\
        print('Allowed values for active status for sport are "True/true or False/false"')

    data_tuple = (name, slug, active_status)

    return data_tuple


def create_sports(_name, _slug, _active_status):

    data_tuple = validate_input(_name, _slug, _active_status)

    if all(data_tuple):
        conn = sqlite3.connect('database/sportsbook.db')
        cur = conn.cursor()
        sql = 'INSERT INTO sport VALUES (?,?,?)'

        try:
            cur.execute(sql, data_tuple)

        except sqlite3.IntegrityError:
            print('duplicate value for name in column sports.name')

        conn.commit()

        conn.close()


def read_sports():

    conn = sqlite3.connect('database/sportsbook.db')

    cur = conn.cursor()
    sql = 'select * from sport'
    cur.execute(sql)
    rows = cur.fetchall()

    conn.close()

    print('--- Sports ---')
    print(' Name | Slug | Active')

    for row in rows:
        print(row)

    print('------------')


def check_sports_active_status(name):

    conn = sqlite3.connect('database/sportsbook.db')

    # select a list of values instead of tuples so that values can be compared
    conn.row_factory = lambda cursor, row: row[0]
    cur = conn.cursor()
    rows = cur.execute("select active from event where sport = ?", (name,)).fetchall()

    print(rows)

    if 'true' in rows or 'True' in rows:
        print(f'Sport {name} is still active')

    # if not all Events are active make the sport inactive
    else:
        update_sport_active_status(name, 'false')
        print(f'The sport {name} is now inactive')


def update_sport_active_status(_name, _status):

    invalid_input = False

    name = _name

    if _status in ('true', 'True', 'false', 'false'):
        status = _status
    else:
        print('Invalid Input for status. Allowed values are "true True false false"')
        invalid_input = True

    if not invalid_input:
        conn = sqlite3.connect('database/sportsbook.db')
        cur = conn.cursor()

        cur.execute('UPDATE sport '
                    'SET active = ?'
                    'where sports_name = ?', (status, name))

        conn.commit()
        conn.close()












