# Author: Isaac Wetton
# Contact: isaac@wetton.net

# Given ASCII .txt input for December and May, the script will:
# Reformat the time so that it is seconds since the beginning of the timeseries.
# Average the magnetic field for timeseries point for each month.
# Calculate the average deviation between the two plots (excluding Ganymede encounter).
# Adjust the May plot using these average values so that it is the same magnitude as the December plot.
# Subtract the May data points from the December data points.

# Imports
import os


# Define Table Class
class Table:
    """
    A data table containing time, JSO coordinate, absolute magnetic field strength, and Galileo-Jupiter and
    Galileo-Ganymede distance data.
    """

    def __init__(self, file="", rows=None):
        """Class initialisation method which sets the received arguments as object attributes"""
        if file != "":
            # Open file, read lines and close file
            f = open(file, "r")
            self.rows = f.readlines()
            f.close()
        elif list:
            self.rows = rows
        else:
            print("No input data submitted")
        # Define table size (number of rows)
        self.size = len(self.rows)

        # Define column data lists
        self.time = []
        self.JSOx = []
        self.JSOy = []
        self.JSOz = []
        self.bmag = []
        self.gal_jup = []
        self.gal_gan = []

        # Assign data to lists
        for i in range(0, self.size):
            row = self.rows[i]
            points = row.split(" ")
            self.time.append(points[0])
            self.JSOx.append(points[1])
            self.JSOy.append(points[2])
            self.JSOz.append(points[3])
            self.bmag.append(points[4])
            self.gal_jup.append(points[5])
            self.gal_gan.append(points[6])

    def update_rows(self):
        """Updates self.rows to include any updated data points in the column data lists"""
        rows = []
        for i in range(0, self.size):
            lsRow = [self.time[i], self.JSOx[i], self.JSOy[i], self.JSOz[i], self.bmag[i], self.gal_jup[i], self.gal_gan[i]]
            rows.append("".join(lsRow))
        self.rows = rows

    def output(self, file):
        """Outputs the data table to a text file"""
        # Open file for writing
        if os.path.exists(file):
            os.remove(file)
        f = open(file, "r")
        self.rows = f.readlines()
        for i in range(0, self.size):
            f.write(self.rows[i])
        f.close()

    def timeformat(self):
        """Reformats the time column to be in seconds since the beginning of the timeseries"""
        start = float(self.time[0])
        for i in range(0, self.size):
            self.time[i] = str(float(self.time[i]) - start)
        self.update_rows()

    def collectav_bmag(self):
        """Returns a new list of times alongside magnetic field strengths. If there are multiple data points for the
        same time, it replaces them with a single data point with the magnetic field averaged at that time. """
        avRows = []
        prev = float(self.time[0])
        totalPointBmag = float(self.bmag[0])
        totalPoints = 1
        for i in range(1, self.size):
            if float(self.time[i]) == prev:
                totalPoints += 1
                totalPointBmag += float(self.bmag[i])
            else:
                avBmag = totalPointBmag / totalPoints
                avRows.append([str(prev), str(avBmag)])
                totalPointBmag = float(self.bmag[i])
                totalPoints = 1
            prev = float(self.time[i])
        avBmag = totalPointBmag / totalPoints
        avRows.append([str(prev), str(avBmag)])
        return avRows
