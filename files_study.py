# open() function is used to open a file (can be any file in the same directory)
the_race = open('turtle_module_study.py')

# The file.close() method closes the file, after which no more reads or writes to the file are allowed
# The file.read() method returns the file contents as a string.
# The file.readlines() method returns a list of strings (elements of list are accessed in the same way using index),
# where the first element is the contents of the first line (index[0]),
# the second element is the contents of the second line and so on.
# Both methods can be given an optional argument that specifies the number of bytes
# the_race.read(500) will read up to 500 bytes

code = the_race.read()  # just reads the file does not show anything on output terminal
# file.readline(), returns a single line at a time, which is useful when dealing with large files

# file.write() method writes a string argument to a file
# only accepts string argument, integers and floating-point values must be converted using str() first

nf = open('files.py', 'w')  # format
nf.write('new file created using files methods')
# this will open the file for writing and overwrite contents of existing file
# If the file does not exist, then the file is created.
nf.close()

# 'r' opens file to read only
# 'a' opens file to append (info is added to end of file) (does not overwrite)
the_race = open('turtle_module_study.py', 'a')
the_race.write('#all notes')
# The 'a+' mode opens the file for both reading and writing, appending new writes.

the_race.close()  # closes the file. (it is important to always close the file)

# A with statement can be used to open a file, execute a block of statements, and automatically
# close the file when complete. The with statement is recommended, because closure of the file is guaranteed.

# A comma-separated values (csv) file (simple text-based file format) uses commas to separate data items, called fields
# contents of csv file
# name,hw1,hw2,midterm,final
# Petr Little,9,8,85,78
# Sam Tarley,10,10,99,100
# Joff King,4,2,55,61


import csv

with open('grades.csv', 'r') as csvfile:
    # csv.reader is the method (inside brackets we mention file name)
    grades_reader = csv.reader(csvfile, delimiter=',')  # delimiter works like the split command
    row_num = 1
    for row in grades_reader:
        print(f'Row #{row_num}: {row}')
        row_num += 1
# output:
# Row #1: ['name', 'hw1', 'hw2', 'midterm', 'final']
# Row #2: ['Petr Little', '9', '8', '85', '78']
# Row #3: ['Sam Tarley', '10', '10', '99', '100']
# Row #4: ['Joff King', '4', '2', '55', '61']