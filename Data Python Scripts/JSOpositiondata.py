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
allowedErr = (0.2, 0.05, 0.05)

# Define input and output files
inputFile = open("input.txt", "r")
if os.path.exists("output.txt"):
    os.remove("output.txt")
outputFile = open("output.txt", "x")




