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

    with open(filename, 'r', newline="") as csvfile:
        file_reader = csv.DictReader(
            csvfile, delimiter=separator, quotechar=quote)
        return file_reader.fieldnames


name_table = read_csv_fieldnames(
    r"D:\python\coursera excersise\dictionary\iterating\table1.csv", ",", ";")
print(name_table)
print("")


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
    with open(filename, 'r', newline='') as csvfile:
      new_list=[]
      file_reader=csv.DictReader(csvfile, delimiter=separator,quotechar=quote)
      for row in file_reader:
        new_dict={}
        for name in row:
          new_dict[name]=row[name]
        new_list.append(new_dict)
    return new_list


print(read_csv_as_list_dict(
    r"D:\python\coursera excersise\dictionary\iterating\table1.csv", ",", ";"))
print("")

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
    new_dict={}
    with open(filename, 'r', newline='') as csvfile:
      file_reader=csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
      for row in file_reader:
        sec_dict={}
        for name in row:
          sec_dict[name]=row[name]
        new_dict[row[keyfield]]=sec_dict
    return new_dict


print(read_csv_as_nested_dict(r"D:\python\coursera excersise\dictionary\iterating\table1.csv", "Joe", ",", ";"))
print("")


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
    with open(filename,'w', newline='') as csvfile:
      file_write = csv.writer(csvfile, fieldnames = fieldnames, delimiter = separator, quotechar = quote)
      file_write.writeheader()
      for value in table:
        file_write.writerow(
          {
          fieldnames[0]:value[fieldnames[0]],
          fieldnames[1]:value[fieldnames[1]],
          fieldnames[2]:value[fieldnames[2]],
          fieldnames[3]:value[fieldnames[3]]
          }
        )


# print(write_csv_from_list_dict(r"D:\\python\\coursera excersise\\dictionary\\iterating\\table2.csv", [{'a':1,'b':2,'c':3,'d':4},    \
#                                                                                                      {'a':5,'b':6,'c':7,'d':8},    \
#                                                                                                      {'a':9,'b':10,'c':11,'d':12}],\
#                                                                                                       ['a', 'b', 'c', 'd'], ',', ';'))
# print(write_csv_from_list_dict(r"D:\python\coursera excersise\dictionary\iterating\number_table.csv", [{'a': 1, 'c': 2, 'b': 3, 'd': 4,}, \
#                                               {'a': 5, 'c': 6, 'b': 7, 'd': 8}, \
#                                               {'a': 9, 'c': 10, 'b': 11, 'd': 12}, \
#                                              ['a', 'b', 'c', 'd'], ',', '"'))

