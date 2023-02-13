# Author: Isaac Wetton
# Contact: isaac@wetton.net

# Imports
from isolation import *
import os

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

# Average the differences in diffAv
totalDiffs = 0
for diff in diffAv:
    if float(diff[0]) < 11500 or float(diff[0]) > 12500:
        totalDiffs += float(diff[1])
adjustment = totalDiffs / len(diffAv)

# Addition of average to May data
for i in range(0, may.size):
    may.bmag[i] = str(float(may.bmag[i]) + adjustment)
may.update_rows()

# Creation of artificial December 2000 field without Ganymede
fakeDec = []
for i in mayAv:
    fakeDec.append([i[0], str(float(i[1]) + adjustment)])

# Subtraction of artificial December data from actual December data
# This data will serve as Ganymede's isolated magnetic field strength
noGan = []
for i in range(0, len(fakeDec)):
    noGan.append([decAv[i][0], str(float(decAv[i][1]) - float(fakeDec[i][1]))])

# Output isolated data
# Open file for writing
if os.path.exists("noGan.txt"):
    os.remove("noGan.txt")
f = open("noGan.txt", "x")
for i in range(0, len(noGan)):
    f.write(" ".join(noGan[i]) + "\n")
f.close()
