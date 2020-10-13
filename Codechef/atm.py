x, y = input().split()              #map(int, input().split())
x = int(x)
y = int(y)
if (x % 5 == 0) and (x < y):
    remaining = (y - x) - 0.50
    print(remaining)
elif x > y:
    print(y)
else:
    print(y)
