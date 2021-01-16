import math
import os
import random
import re
import sys



if __name__ == '__main__':

    t = int(input())
    BIT = []
    for t_itr in range(t):
        n, k = map(int, input().split())

        for i in range(1, n):
            for j in range(2, n + 1):
                if i != j and i < j:
                    bit_and = i & j
                    if bit_and < k:
                        BIT.append(bit_and)
                        
        if max(BIT) < k:
            print(max(BIT))
        BIT.clear()