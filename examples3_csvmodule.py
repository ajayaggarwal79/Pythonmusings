"""
Using the csv module.
"""

import csv
from __future__ import print_function

def parse(csvfilename):
    """
    Reads CSV file named csvfilename, parses
    it's content and returns the data within
    the file as a list of lists.
    """
    table = []
    with open(csvfilename, "r") as csvfile:
        csvreader = csv.reader(csvfile,
                               skipinitialspace=True)
        for row in csvreader:
            table.append(row)
    return table


def print_table(table):
    """
    Print out table, which must be a list
    of lists, in a nicely formatted way.
    """
    for row in table:
        # Header column left justified
        print("{:<19}".format(row[0]), )
        # Remaining columns right justified
        for col in row[1:]:
            print("{:>4}".format(col),)
        print("", )

table = parse("hightemp.csv")
print_table(table)

print("")
print("")

table2 = parse("hightemp2.csv")
print_table(table2)
