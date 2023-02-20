import os

allowedZ = (-0.1, 0.1)
allowedY = (-1.0, 1.0)

inputFile = open("input.txt", "r")
if os.path.exists("output.txt"):
    os.remove("output.txt")
outputFile = open("output.txt", "x")

lsInput = inputFile.readlines()

for i in range(0, 694363):
    dataPoint = lsInput[i].split("  ")
    if allowedY[0] < float(dataPoint[2]) < allowedY[1] \
            and allowedZ[0] < float(dataPoint[3]) < allowedZ[1]:
        output = ""
        for x in dataPoint:
            output += " " + x
        outputFile.write(output)
        
# Close input and output files
inputFile.close()
outputFile.close()

