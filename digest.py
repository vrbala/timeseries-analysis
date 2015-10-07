#! /usr/bin/python

import os
import sys
import csv
import re

if len(sys.argv) < 2:
    print "Pass input file as the only argument."
    sys.exit(0)

inFile = sys.argv[1]

csvHandle = None
csvWriter = None

with open(inFile) as f:
    lastCputime = 0
    startTimestamp = 0
    for line in f.readlines():
        line = line.rstrip('\n')
        if line.startswith('#'):

            # one digest file per pass
            m = re.match('# pass (\d+)', line)
            if m is not None:
                csvFile = './digest.%s.csv' % m.group(1)
                if os.path.exists(csvFile):
                    os.remove(csvFile)

                csvHandle = open(csvFile, 'w')
                csvWriter = csv.writer(csvHandle)
                # csv header
                csvWriter.writerow(['timestamp', 'cputime'])

                # reset last cpu time and start time for each repetition
                lastCputime = 0
                startTimestamp = 0
        else:
            timestamp, times = line.split()
            timestamp = float(timestamp)
            if startTimestamp == 0:
                startTimestamp = timestamp
            times = times.split(',')
            user,system = map(float, times[:2])
            csvWriter.writerow([timestamp-startTimestamp,
                                lastCputime+user+system])

            if len(times) == 3: # summary line
                lastCputime += user+system

# close the output file
csvHandle.close()
