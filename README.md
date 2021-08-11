This project imitates the working of a sportsbook application.  It has been coded entirely in Python3. The database used is sqlite3.

**Tables**

There are 3 tables in this application. These will be created in the 'database' folder.
1. Sports
2. Events
3. Selections

Sports - This table has entries for the currently active sports. There are 3 columns in this table. Sports name is the primary key. Slug column has a url for the sport. Active column shows whether the sport is active or not. 

Events - Shows events on which bets can be placed on. There can be multiple events for one sport. There are 8 columns in this table. Event name is the primary key.

Selections - This table has entries for current bets. There are 5 columns in this table. Selection name is the primary key.


**Code**

There are 4 modules in this project.

1. Sports - It has all the functions related to the Sports table. Sports can be added, read from the table and updated. Some basic validatios are performed while adding a new sport. Such as the name and url of the sport cannot be empty. Also, only specific values are allowed for the active column. Duplicate values for primary key column are not allowed. The status of a sport can be updated.
   
2. Events - Similar to sports module, it has functions related to events table. Events can be created, read from the table and updated. Allowed updates are changing the status of an event and changing the active status of an event. There is a module to check the active status of a Sport. If all the events of a sport are inactive then the sport will also be inactive.
   
3. Selection - This module has functions related to the selections table. Selections can be created, read from the table and updated. Basic validations are performed here too. Such as the price should be in a numeric format with exactly two numbers after decimal. Allowed updates are outcome of an event and status of an event. This module also checks if all the selections of an event are active. If all the selections are inactive the event too will become inactive.
   
4. Search - This module has 2 search functions. A search can be performed on any of the 3 tables by a keyword. For e.g. Searching for 'ireland' in 'selection' will list all selections involving Ireland.The second search function can be used to search for events starting before, after or at a particular time. No validations have been performed on time. So it is expected to use correct format of time while searching. e.g. '2021-09-15 09:30:00'

5. main - Main module is used to run the project. New sports, events and selected can be created, read or updated using this module.


**Scripts**

This project has 2 scripts.

1. Create Table - This is used for creating fresh tables used in the project. If the tables are already present it will delete the tables and create them again.

2. Populate tables- This is used to populate the tables by reading the corresponding csv file for each table. The files are located in the 'inputs' folder.

**Tests**

Test1 - This test is used to verify whether an event becomes inactive once all its selections are inactive. After using the script to populate the tables, there will be 2 selections for the event 'ireland vs england football match'. They are 'ireland to win ireland vs england football match' and 'england to win ireland vs england football match'. Test1 updates the status of the outcome of these selections and also the active status for these selections. Once these selections are inactive, the event 'ireland vs england football match' should become inactive too. This can be verified using in the output of read_event() function in this test. If this test is run for the second time the vent will show inactive at the beginning. In this case the tables need to be created using the scripts 'create table' and 'populate table' and then the test can be run again.

Test2 - This test is used to verify whether a sport becomes inactive once all its events are inactive. The sport 'football' had 2 events - 'ireland vs england football match' and 'ireland vs germany football match'. Test1 makes the first event inactive. Test2 is used to make the event 'ireland vs germany football match' by making its selections inactive. At the end of test2 , the sport 'football' should become inactive too.

Test3 - This test has some search functions that can be performed on the table. It can also be used to look for events before, after or at a particular time.

**How to run the project** 

The scripts create table and populate tables should be run first. Then either the main code or tests can be run. However test1 should be run before test2. 
