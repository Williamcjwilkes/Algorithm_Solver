'''
Validation Functions

Created: 04/05/2023
Last updated: 04/05/2023

Author: William Charles Jeffery Wilkes
'''

import os
import Algorithm_Functions

#functionn for validating the string is a path and a valid filename
def is_valid_filename(filename):
    # Check if the path to the file exists
    if not os.path.exists(filename):
        print(f"Error: path '{filename}' does not exist.")
        return False
    
    # Get the filename from the path
    filename = os.path.basename(filename)
    
    # Check if the filename contains any illegal characters based on the operating system
    illegal_chars = set('<>:"/\\|?*')
    if any(char in illegal_chars for char in filename):
        print(f"Error: filename '{filename}' contains illegal characters.")
        return False

    # if filename is valid will return True
    return True

#Function for validating the string for the algorithm.
def is_lowercase_alpha(string):
    # Remove whitespace
    string = ''.join(string.split()).lower()
    # Check if all characters are alphabetical and lowercase
    if string.isalpha() and string.islower():
        return True
    else:
        print("Error: sorting algorithm '{string}' could not be determined.")
        return False



