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

#matches = []
with open(filename) as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        i += 1
        
        # skipping the headline
        if i < 5: continue
        if len(row) != 6: break

        print("Inserting: {0!}".format(row))
        teamA = row[0].strip()
        teamB = row[1].strip()
        field = row[2].strip()

        match_time = time.strptime(row[4].strip(), "%m/%d/%y %a")

        day = int((time.mktime(match_time) - time.mktime(start_date))/(60*60*24)) + 1

        match_time = row[5].strip()[:5]


        print("Got back: {0!}".format(t.add_match(teamA, teamB, day, field, match_time, group)))
        
        #matches.append((teamA, teamB, field, day, match_time))

