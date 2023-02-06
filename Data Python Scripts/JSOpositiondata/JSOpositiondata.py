# This script will analyse a dataset with format:
# DATA_COLUMNS : SECS FROM 1970-01-01, gll_xyz_jso[0], gll_xyz_jso[1], gll_xyz_jso[2],
# gll_mag_msreal_Mag_7523700765402304842, gll_r_jup_7523700765402304842, gll_orb_ga_RANGE_SPRH_7523700765402304842

# Given JSO coordinates and allowed difference, the script will output a data file containing only data
# where the craft's position was within those parameters.

# Imports
import os

# Galileo position x, y, z (December 2000 Ganymede Flyby)
galPos = (-15.2, 0.57, 0.84)
# Allowed ranges
allowedErr = (5, 1, 1)

# Define input and output files
inputFile = open("input.txt", "r")
if os.path.exists("output.txt"):
    os.remove("output.txt")
outputFile = open("output.txt", "x")

# Read input data into a list
lsInput = inputFile.readlines()

for i in range(1, 207357):
    dataPoint = lsInput[i].split("     ")
    if galPos[0] - allowedErr[0] < float(dataPoint[1]) < galPos[0] + allowedErr[0] \
            and galPos[1] - allowedErr[1] < float(dataPoint[2]) < galPos[1] + allowedErr[1] \
            and galPos[2] - allowedErr[2] < float(dataPoint[3]) < galPos[2] + allowedErr[2]:
        output = ""
        for x in dataPoint:
            output += " " + x
        outputFile.write(output)

# Close input and output files
inputFile.close()
outputFile.close()
