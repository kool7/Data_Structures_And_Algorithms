
def maxDiff(arr, arr_size):
    max_diff = arr[1] - arr[0]

    for i in range(0, arr_size):
        for j in range(i + 1, arr_size):
            if(arr[j] - arr[i] > max_diff):
                max_diff = arr[j] - arr[i]

    return max_diff

arr = [1, 2, 90, 10, 110] 
size = len(arr) 
print ("Maximum difference is", maxDiff(arr, size)) 

    
def maxDiff2(arr, arr_size): 
    max_diff2 = arr[1] - arr[0] 
    min_element = arr[0] 
      
    for i in range( 1, arr_size ): 
        if (arr[i] - min_element > max_diff2): 
            max_diff2 = arr[i] - min_element 
      
        if (arr[i] < min_element): 
            min_element = arr[i] 
    return max_diff2 
      
# Driver program to test above function  
arr = [1, 2, 6, 80, 100] 
size = len(arr) 
print ("Maximum difference is",  
        maxDiff2(arr, size)) 
