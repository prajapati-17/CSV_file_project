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
    """

    with open(filename, 'r') as csvfile:
        table = []
        file_reader = csv.reader(
            csvfile, delimiter=separator, quotechar=quote)
        for row in file_reader:
            table.append(row)
    return table


def print_table(new_table):
    for row in new_table:
        print(row)


name_table = read_csv_fieldnames(
    r"D:\python\coursera excersise\dictionary\iterating\name_table.csv", ",", ";")
print_table(name_table)
print("")
