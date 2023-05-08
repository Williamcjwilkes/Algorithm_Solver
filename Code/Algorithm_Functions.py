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

            
#implements the Merge Sort algorithm.
def Merge_Sort(arr):
    if len(arr) > 1:
        # Divide the array into two arrays
        mid = len(arr)//2
        # Dividing the array elements into 2 halves
        L = arr[:mid]
        R = arr[mid:]
        # Sorting the two arrays and the divide them. 
        Merge_Sort(L)
        Merge_Sort(R)
        
        i = j = k = 0
        
        # Merge the sorted sub arrays back into the original array
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    
#implements the Bubble Sort algorithm.
def Insertion_Sort():
    print("user selected Insertion_Sort algorithm") 
    
#implements the Bubble Sort algorithm.
def Quick_Sort():
    print("user selected bQuick_Sort algorithm") 
    
