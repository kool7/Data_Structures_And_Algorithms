T = int(input())
for i in range(T):
    first = int(input())
    if first <= 10:
        inp = [int(x) for x in input().split()]
        inp.sort(reverse=True)
        ma = max(inp)
        x = [ma]
        y = []

        for i in inp[1:]:
            if i <= ma and sum(y) <= ma:
                y.append(i)
            else:
                x.append(i)

    n = max(sum(x), sum(y))
    print(n)