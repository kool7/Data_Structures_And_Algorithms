# import math
# import os
# import random
# import re
# import sys

# arr_count = int(input())
# arr = list(map(int, input().rstrip().split()))

# def reverseArray(a):
#     new_list = a[::-1]
#     return new_list

# reverseArray(arr)
arr_count = int(input())
arr = list(map(int, input().rstrip().split()))

new = arr[::-1]
print(new)