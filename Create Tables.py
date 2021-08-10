import sqlite3

# Create a new connection to connect to sportsbook database

conn = sqlite3.connect('database/sportsbook.db')
cur = conn.cursor()

# Drop tables if they already exist

sql = "DROP TABLE IF EXISTS sport"
cur.execute(sql)

sql = "DROP TABLE IF EXISTS event"
cur.execute(sql)

sql = "DROP TABLE IF EXISTS selection"
cur.execute(sql)

# Create fresh tables sport, event and selection

sql = "CREATE TABLE IF NOT EXISTS sport(sports_name text primary key, slug text, active text);"
cur.execute(sql)

sql = "CREATE TABLE IF NOT EXISTS event(event_name text primary key, slug text, active text, " \
      "type text, sport text, status text, " \
      "scheduled_start text, actual_start text);"
cur.execute(sql)

sql = "CREATE TABLE IF NOT EXISTS selection(selection_name text primary key, event text," \
      " price text, active text, outcome text);"
cur.execute(sql)

# Commit the changes
conn.commit()

# Close the connection
conn.close()



