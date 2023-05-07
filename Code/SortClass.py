'''
SortClass Functions

Created: 03/05/2023
last updated: 07/05/2023

Author: William Charles Jeffery Wilkes
'''

from cgitb import text
import csv
from os import write
import os.path

class sortClass:
    unsortedArray = []
    sortedArray = []
    timeToSort = 0
    
    def __init__(self, inputFile , outputFile, algorithm):
        self.inputFile = inputFile
        self.outputFile = outputFile
        self.algorithm = algorithm  
         
    def __str__(self):
        return f"The class was created successfully\nInput:{self.inputFile}\nOutput:{self.outputFile}\nAlgorithm Selected:{self.algorithm}"

    def readFile(self):
        with open(self.inputFile, "r") as file:
            string_array = file.read().strip()
            self.unsortedArray = [int(s) for s in string_array.split(',')]
            
        return self.unsortedArray

    
    def writeFile(self):
        # open the output file in append mode
        with open(self.outputFile, 'a') as Write:
            Write.write(str(f"\nThe Algorithm Program {self.algorithm} Edition\n"))

            Write.write(f"\nnThe filepath for the input is: {self.inputFile}\nThe filepath for the output is: {self.outputFile} \nThe algorithm selected was: {self.algorithm}\n")
            
            Write.write(str("\n The unsorted array is:\n"))
            # write each value in the unsorted array to the file
            for value in self.unsortedArray:
                Write.write(str(value) + ' ')
                
            Write.write(str("\n\n The sorted array is:\n"))
            # write each value in the sorted array to the file
            for value in self.sortedArray:
                Write.write(str(value) + ' ')
            Write.write(str("\n\n--------------------------------------------------------------------------------------------------------"))
        print(f"The program has written your txt file to {self.outputFile}")


    