def find(s, ch):
    return [i + 1 for i, ltr in enumerate(s) if ltr == ch]

T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    S = input()
    if len(S) == N:
        I = find(S, "I")
        M = find(S, "M")
        X = find(S, "X")
        Sh = find(S, ":")

        # P = K + 1 - I - M - Sh
        # print(P)

    print(I)
    print(M)
    print(X)
    print(Sh)