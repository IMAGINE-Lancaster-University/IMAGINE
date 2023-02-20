# Author: Isaac Wetton
# Contact: isaac@wetton.net

# Imports
from isolation import *
import os

# Create data tables for May 2000 and Feb 2000 data from text files
feb = Table(file="feb.txt")
may = Table(file="may.txt")

# Format the time to seconds since beginning of timeseries
feb.timeformat()
may.timeformat()

# Average magnetic field strength for each time point
mayAv = may.collectav_bmag()
febAv = feb.collectav_bmag()
print(mayAv)
# Generate list of differences in average for each time point
diffAv = []
for i in mayAv:
    for j in febAv:
        if i[0] == j[0]:
            diffAv.append([i[0], str(float(j[1]) - float(i[1]))])

# Average the differences in diffAv
totalDiffs = 0
for diff in diffAv:
    if float(diff[0]) < 6800 or float(diff[0]) > 7600:
        totalDiffs += float(diff[1])
adjustment = totalDiffs / len(diffAv)

# Addition of average to Feb data
for i in range(0, feb.size):
    feb.bmag[i] = str(float(feb.bmag[i]) + adjustment)
feb.update_rows()

# Creation of artificial December 2000 field without Ganymede
fakeMay = []
for i in febAv:
    fakeMay.append([i[0], str(float(i[1]) + adjustment)])

# Subtraction of artificial December data from actual December data
# This data will serve as Ganymede's isolated magnetic field strength
noGan = []
for i in range(0, len(mayAv)):
    noGan.append([mayAv[i][0], str(float(mayAv[i][1]) - float(fakeMay[i][1]))])

# Append Galileo-Ganymede distance to data
for i in range(0, len(noGan)):
    noGan[i].append(may.gal_gan[i])

# Output isolated data
# Open file for writing
if os.path.exists("noGan.txt"):
    os.remove("noGan.txt")
f = open("noGan.txt", "x")
for i in range(0, len(noGan)):
    f.write(" ".join(noGan[i]))
f.close()
