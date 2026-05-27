import csv

# CSV, JSON and XML are data sterilization formats used to store data as plain texts files
# sterilization means u converts data into a string to save your program’s work to a text file,
# transfer it over an internet connection, or even just copy and paste it into an email.

# u can easily use open() to read them with Python
# but it's easier to use modules to handle them

# CSV: Comma Separated Value
# simplified spreadsheet format, and works best
# for storing a variable number of rows of data that share the same columns.
# You can think of CSV files as a list of lists of values.

# reading csv files
example = open('example.csv')
read_example = csv.reader(example)
data_example = list(read_example)
print(data_example)
print(data_example[0][0]) # First row, first column
print(data_example[0][1]) # First row, second column

#using a for loop to access data
for row in data_example:
    print(str(row))

# writing csv files
example_file = open('example.csv', 'w', newline='')
example_writer = csv.writer(example_file)
example_writer.writerow(['3/15/2065 6:30','Mangoes',34])
example_writer.writerow(['2/20/2055 14:15','Dragonfruits',69])
example_file.close()


# JSON: Javascript Object Notation
# uses the same syntax as objects, arrays, and data types


# XML: Extensible Markup Language
# older, more established data serialization format widely used in enterprise software,
# but is overly complicated to work with if you don’t need its advanced features.