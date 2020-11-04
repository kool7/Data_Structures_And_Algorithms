import math

def is_prime(n):
    if n == 1:
        return False

    max_div = math.floor(math.sqrt(n))
    for i in range(2, max_div + 1):
        if n % i == 0:
            return False
    return True

def is_prime_v2(n):
    if n == 1:
        return False  
    
    if n == 2:
        return False

    if n > 2 and n % 2 == 0:
        return False

    max_div = math.floor(math.sqrt(n))
    for i in range(3, max_div + 1, 2):
        if n % i == 0:
            return False
    
    return True

T = int(input())
for i in range(T):
    num = int(input())

    if is_prime(num):
        print("Prime")
    else:
        print("Not prime")
