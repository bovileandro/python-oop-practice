"""
From "Python: Beyond the Basics - Object Oriented Programming" by D. Blaikie
https://www.safaribooksonline.com/library/view/python-beyond-the/9781771373609/video211128.html

Assignment:
- Create a parent class and subclass it twice with LogFile and DelimFile classes
- Write method in both - should be added to parent
- Write method differences in child classes:
    - Logfile takes a string and writes to file with the date and time
      in the format YYYY-MM-DD HH:MM:SS
    - DelimFile takes a list of delimited data and writes to a file; bonus points
      for enabling user to put in values with a comma in them (e.g. ['4', '2,4', '7'])

"""

import csv
from time import strftime as st


class WriteFile(object):
    def write(self, message, filename):
        with open(filename, 'w', newline='') as csvfile:
            new_row = csv.writer(csvfile, delimiter, ',')


class LogFile(WriteFile, filename):
    #new_row.writerow(st("%Y-%m-%d %H:%M:%S"), message)
    pass

class DelimFile(WriteFile, filename, delimiter):
    pass
