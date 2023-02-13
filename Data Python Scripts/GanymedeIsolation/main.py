# Author: Isaac Wetton
# Contact: isaac@wetton.net

# Imports
from isolation import *

# Create data tables for May 2000 and December 2000 data from text files
dec = Table(file="dec.txt")
may = Table(file="may.txt")

# Format the time to seconds since beginning of timeseries
dec.timeformat()
may.timeformat()

# Average magnetic field strength for each time point
mayAv = may.collectav_bmag()
decAv = dec.collectav_bmag()

# Generate list of differences in average for each time point
diffAv = []
for i in mayAv:
    for j in decAv:
        if i[0] == j[0]:
            diffAv.append([i[0], str(float(j[1]) - float(i[1]))])

