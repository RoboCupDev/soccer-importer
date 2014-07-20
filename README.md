soccer-importer
===============

Scripts for facilitating the process of importing and updating data from RCJ Soccer league


Usage
-----


**import-matches.py**

    $ ./import-matches.py  http://localhost:1337 ./schedule.csv '07/21/14 Mon' 'some group' 12345

The arguments are as follows:

- URL: url of the actual `tournamenter` endpoint
- FILENAME: path to the file in which the CSV export is stored (typically
  schedule.csv)
- STARTDATE: the starting date of the competition (used for computing the day
  on which a particular match is to be played)
- GROUPNAME: the name of a group into which the matches described in FILENAME
  belong to
- PASSWORD: optional parameter, in case the endpoint requires one


**update-matches.py**


    $ ./import-matches.py  http://localhost:1337 ./teamResults.csv '07/21/14 Mon' 'some group' 12345

The arguments are as follows:

- URL: url of the actual `tournamenter` endpoint
- FILENAME: path to the file in which the CSV export is stored (typically
  teamResults.csv)
- STARTDATE: the starting date of the competition (used for computing the day
  on which a particular match is to be played)
- GROUPNAME: the name of a group into which the matches described in FILENAME
  belong to
- PASSWORD: optional parameter, in case the endpoint requires one


