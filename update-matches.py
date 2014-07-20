#!/usr/bin/env python

import sys
import csv
import time

if len(sys.argv) < 5:
    print("usage: {0} URL FILE STARTDATE GROUP [PASSWORD]".format(sys.argv[0]))
    sys.exit(1)

from tournamenter import Tournamenter

url = sys.argv[1]
filename = sys.argv[2]
start_date = time.strptime(sys.argv[3], "%m/%d/%y %a")
group = sys.argv[4]
password = sys.argv[5] if len(sys.argv) >= 6 else ''


t = Tournamenter(url, password)

with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        
        if len(row) != 5:
            continue
        
        if row[0] == 'Home':
            continue


        print("Inserting: {0!r}".format(row))
        teamA = row[0].strip()
        teamB = row[1].strip()
        field = row[2].strip()

        match_time = time.strptime(row[3].strip(), "%A  %d %b %Y")

        day = int((time.mktime(match_time) - time.mktime(start_date))/(60*60*24)) + 1


        r = row[4].split('-')

        teamAScore = r[0][1:]
        teamBScore = r[1][:1]

        print('Got back: ', t.update_match(teamA, teamB, field, day,
            teamAScore, teamBScore, state="ended"))


