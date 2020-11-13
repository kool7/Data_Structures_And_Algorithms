# def find(s, ch):
#     return [i + 1 for i, ltr in enumerate(s) if ltr == ch]


T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    S = input()
    F = []
    ANS = 0
    if len(S) == N:
        for i in range(N):
            if S[i] == 'M':
                F.append(i)
                continue
            elif S[i] == 'I':
                F.append(i)
                continue
                P = K + 1 - F[1] - F[0]
                if P > 0:
                    ANS += 1

            elif S[i] == ':':
                F.append(i)
                continue
            elif S[i] == 'X':
                F.append(i)
                break

            # P = K + 1 - F[0] - F[1] - F[3]

        print(F)
        print(ANS)