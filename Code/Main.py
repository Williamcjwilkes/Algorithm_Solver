'''
The Algorithm Problem 

Created: 04/05/2023
last updated: 06/05/2023

Author: William Charles Jeffery Wilkes
'''

#import 
import Functions
import SortClass
import Algorithm_Functions

import sys
import re
import csv
import os

# validate the args passed in the program.
if len(sys.argv) == 4:
    print ("Arguments accepted: validating please wait...")
else:
    if len(sys.argv) < 4:
        print("Arguments not accepted: There are few many arguments")
        exit()
    else: 
        print ("Arguments not accepted: There are many many arguments")
        exit()
#checks the arguments passed in the program and validates them.
if Functions.is_valid_filename(sys.argv[1]) and Functions.is_valid_filename(sys.argv[2]) and Functions.is_lowercase_alpha(sys.argv[3]):
    print("Arguments are valid")
else:
    print("Arguments are not valid")
    exit()
    
#create the sort class now the arguments are validated.
sorting = SortClass.sortClass(sys.argv[1],sys.argv[2],sys.argv[3])
sorting.readFile()

sorting.sortedArray = sorting.unsortedArray.copy()

if sorting.algorithm == "bubble" or "bubblesort":
    Algorithm_Functions.Bubble_Sort(sorting.sortedArray)
elif sorting.algorithm == "merge" or "mergesort":
    Algorithm_Functions.Merge_Sort(sorting.sortedArray)

#tesing the outputfile
sorting.writeFile()

exit()  

    
 
#sort program arguments

