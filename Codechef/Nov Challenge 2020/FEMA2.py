T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    S = input()

    i = 0
    j = 0
    sheet = 0
    ANS = 0
  
    while (i < N or j < N):
        if i == S.find('M', i):
            print(f'first ith loop {i}')
            if j == S.find('I', j):
                if (i > j):
                    for k in range(j, i + 1):
                        if k == S.find(':'):
                            sheet += 1

                    P = K + 1 - j - 1 - sheet

                    if P > 0:
                        ANS += 1
                        i += 1
                        j += 1
                        sheet = 0

                    if P <= 0:
                        if(i<j):
                            i += 1
                        else:
                            j += 1

                elif (i < j):
                    for k in range(i, j + 1):
                        if k == S.find(':', k):
                            sheet += 1
                    print(sheet)
                    P = K + 1 - j - 1 - sheet
                    
                    if P > 0:
                        ANS += 1
                        i += 1
                        j += 1
                        sheet = 0
                        print(ANS)
                        print(f'i loop {i}')
                        print(f'j loop {j}')

                    if P <= 0:
                        if(i<j):
                            i += 1
                        else:
                            j += 1

                print(f'first jth loop {j}')

            elif j == S.find('X', j):
                i = j
                j += 1
                i += 1
                print(f'second jth loop {j}')
            else:
                j += 1
                print(f'third jth loop {j}')

        elif i == S.find('X', i):
            j = i
            i += 1
            j += 1
            print(f'second ith loop {i}')
        else:
            i += 1
            print(f'third ith loop {i}')

    print(ANS)