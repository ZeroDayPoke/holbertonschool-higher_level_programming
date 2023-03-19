#!/usr/bin/python3
"""
Write a function that inserts a line of text to a file, after each
line containing a specific string (see example):

Prototype: def append_after(filename="", search_string="", new_string=""):

You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module
"""


def append_after(filename="", search_string="", new_string=""):
    """Open the file for reading and writing using the with statement"""
    with open(filename, 'r+') as fred:
        """Read the lines of the file into a list"""
        lines = fred.readlines()
        """Reset the file pointer to the beginning of the file"""
        fred.seek(0)
        """Iterate over the lines in the list"""
        for line in lines:
            """Write the current line to the file"""
            fred.write(line)
            """If the line contains the search string, append
            the new string to the file"""
            if search_string in line:
                fred.write(new_string)
        """Truncate the file after the last line
        to remove any remaining content"""
        fred.truncate()
