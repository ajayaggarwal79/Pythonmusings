"""
Using csv.DictReader.
"""

import csv

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr',
          'May', 'Jun', 'Jul', 'Aug',
          'Sep', 'Oct', 'Nov', 'Dec')

def dictparse(csvfilename, keyfield):
    """
    Reads CSV file named csvfilename, parses
    it's content and returns the data within
    the file as a dictionary of dictionaries.
    """
    table = {}
    with open(csvfilename, "rt",) as csvfile:
        csvreader = csv.DictReader(csvfile,
                                   skipinitialspace=True)
        for row in csvreader:
            table[row[keyfield]] = row
    return table


def print_table(table):
    """
    Print out table, which must be a dictionary
    of dictionaries, in a nicely formatted way.
    """
    print "City               ",
    for month in MONTHS:
        print"{:>6}".format(month), 
    print("")
    for name, row in table.items():
        # Header column left justified
        print"{:<19}".format(name), 
        # Remaining columns right justified
        for month in MONTHS:
            print"{:>6}".format(row[month]), 
        print"", 

table = dictparse("hightemp.csv", 'City')
print_table(table)
