#Code by COPYASSIGNMENT.COM
#Implementation of Bubble Sort 
  
def bubbleSort(arr): 
    n = len(arr) 
  
    #Traversing through all array elements 
    for i in range(n): 
        for j in range(0, n-i-1): 
  
            #Traversing the array from 0 to n-i-1 
            #Swap if the element found is greater than the next element 
            if arr[j] > arr[j+1] : 
                #Swapping
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                
# Driver code
arr = [64, 34, 25, 12, 22, 11, 90] 

#Printing original array
print("Original Array : ", arr)  

#Calling Function
bubbleSort(arr) 

#Printing Sorted Array  
print ("Final Sorted array : ", arr) 
