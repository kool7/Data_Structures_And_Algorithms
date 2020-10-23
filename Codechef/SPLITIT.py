t = int(input().strip())
for i in range(t):
    n = int(input())
    s = input()
    last=s[n-1]
    if last in s[:n-1]:
        print('Yes')
    else:
        print('No')