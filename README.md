This project imitates the working of a sportsbook application.  It has been coded entirely in Python3. The database used is sqlite3.

**Tables**

There are 3 tables in this application.
1. Sports
2. Events
3. Selections

Sports - This table has entries for the currently active sports. There are 3 columns in this table. Sports name is the primary key. Slug column has a url for the sport. Active column shows whether the sport is active or not. 

Events - Shows events on which bets can be placed on. There can be multiple events for one sport. There are 8 columns in this table. Event name is the primary key.

Selections - This table has entries for current bets. There are 5 columns in this table. Selection name is the primary key.

**Code**

There are 2 Scripts, 4 modules and 3 tests in this project.