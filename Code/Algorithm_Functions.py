'''
Algorithm functions

Created: 04/05/2023
last updated: 07/05/2023

Author: William Charles Jeffery Wilkes
'''

#implements the Bubble Sort algorithm.
def Bubble_Sort(arr):
    # length of the array
    lengthOfArr = len(arr)
    for i in range(lengthOfArr - 1):
        for j in range(lengthOfArr - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

            
#implements the Bubble Sort algorithm.
def Merge_Sort():
    print("user selected Merge_Sort algorithm") 
    
#implements the Bubble Sort algorithm.
def Insertion_Sort():
    print("user selected Insertion_Sort algorithm") 
    
#implements the Bubble Sort algorithm.
def Quick_Sort():
    print("user selected bQuick_Sort algorithm") 
    
