"""
    Extract a CSV file with header, create a list of dicitonaries for the CSV,
    read in a file as a dictionary of dicitonaries and
    write out a file using fieldnames so it is ordered.
"""
import csv
def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      A list of strings corresponding to the field names in 
      the given CSV file.

    Given a CSV file, read the data into a nested list
    Input: String corresponding to comma-separated  CSV file
    Output: Lists of lists consisting of the fields in the CSV file
    """

    table=[]
    with open(filename, "r") as csvfile:
        csvreader=csv.reader(csvfile,delimiter=separator, quotechar=quote)
        for row in csvreader:
            table.append(row)
    return table[0]

#print(read_csv_fieldnames('table1.csv', ',', '"'))


def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """

    with open(filename, "r") as csvfile:
        tab = [{k: v for k, v in row.items()}
             for row in csv.DictReader(csvfile,delimiter=separator, quotechar=quote)]
        return tab

##import csv
##dict_key={}
##tup=()
##lst=[]
##lst1=[]
##with open('\\\\USHOUHOME02\\rajua1\\Desktop\\Python\\table1.csv', 'r') as csvfile:
##    reader = csv.DictReader(csvfile)
##    for row in reader:
##        for k,v in row.items():
##            lst.append((k,v))
##        dict_key=dict(lst)
##        print(dict_key) 
            


    
    
def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the 
      field values for that row.
    """

    table = {}
    with open(filename, "r") as csvfile:
        csvreader = csv.DictReader(csvfile,delimiter=separator, quotechar=quote)
        for row in csvreader:
            table[row[keyfield]] = row
    return table

def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """

    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, delimiter=separator, quotechar=quote,
                                    fieldnames=fieldnames, quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()

        for row in table:
            csv_writer.writerow(row)
    
