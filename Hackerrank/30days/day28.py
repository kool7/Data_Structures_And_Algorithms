import re 
import os

T = int(input())
data = []

for i in range(T):
    name, email = map(str, input().split())
    if email.endswith('@gmail.com'):
        data.append(name)

data.sort()  
print(*data, sep='\n')