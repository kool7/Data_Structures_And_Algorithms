def maxDiff(arr, arr_size):
    max_diff = arr[1] - arr[0]

    for i in range(0, arr_size):
        for j in range(i + 1, arr_size):
            if(arr[j] - arr[i] > max_diff):
                max_diff = arr[j] - arr[i]

    return max_diff

arr = [5, 28, 3, 9, 98, 2, 1, 55] 
size = len(arr) 
print ("Maximum difference is", maxDiff(arr, size)) 


n = int(input("Enter number here: ").strip())

if n % 2 != 0:
    print("Weird")
elif(n % 2 == 0) and (n in range(2,6)):
    print("Not Weird")
elif(n % 2 == 0) and (n in range(6, 21)):
    print("Weird")
elif(n % 2 == 0) and (n > 20):
    print("Not Weird")
