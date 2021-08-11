import sqlite3


def search_name_having(_table, _keyword):

    keyword = '%' + _keyword + '%'

    invalid_input = False

    if _table in ('sport', 'event', 'selection'):
        table = _table

        if table == 'sport':
            name = 'sport_name'

        if table == 'event':
            name = 'event_name'

        if table == 'selection':
            name = 'selection_name'

    else:
        invalid_input = True
        print('Table name incorrect for query. Allowed values are sport, event or selection')

    if not invalid_input:

        sql = f'select * from {table} where {name} like ?;'

        conn = sqlite3.connect('database/sportsbook.db')

        cur = conn.cursor()
        cur.execute(sql, (keyword, ))

        rows = cur.fetchall()

        print(f'The {table}s having {_keyword} are :')

        for row in rows:
            print(row)

        print('----------------------')


def event_schedule_time(_comparison, time):

    invalid_input = False

    if _comparison in ('before', 'after', 'at'):
        comparison = _comparison

        if comparison == 'before':
            operator = '<='

        if comparison == 'after':
            operator = '>='

        if comparison == 'at':
            operator = '='

    else:
        invalid_input = True
        print('incorrect comparator. Allowed values are before, after or at')

    if not invalid_input:

        sql = f'select event_name, scheduled_start from event where scheduled_start {operator} ?;'

        conn = sqlite3.connect('database/sportsbook.db')

        cur = conn.cursor()
        cur.execute(sql, (time, ))

        rows = cur.fetchall()

        print(f' Events {comparison} {time} | Scheduled Start Time')

        for row in rows:
            print(row)

        print('----------------------')
