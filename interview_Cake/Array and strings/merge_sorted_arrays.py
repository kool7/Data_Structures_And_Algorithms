# In order to win the prize for most cookies sold, 
# my friend Alice and I are going to merge our Girl Scout Cookies orders and enter as one unit.

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

def sortedArrays(array1:list, array2:list):

    return sorted(array1 + array2)

print(sortedArrays(my_list, alices_list))
