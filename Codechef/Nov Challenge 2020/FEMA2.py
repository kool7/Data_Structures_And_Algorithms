T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    S = input()
        
    MAGNET = 0
    IRON  = 0
    ANS = 0
    SHEET = 0
  
    while (MAGNET < N and IRON < N):
    
        if MAGNET == S.find('M', MAGNET):
            
            if IRON == S.find('I', IRON):

                if MAGNET > IRON:
                    for i in range(IRON, MAGNET + 1):
                        if i == S.find(':', i):
                            SHEET += 1
                    
                    P = K + 1 - abs(IRON - MAGNET) - SHEET
        
                    if P > 0:
                        ANS += 1
                        MAGNET += 1
                        IRON += 1
                        SHEET = 0

                    else:
                        if IRON < MAGNET:
                            IRON += 1
                        else:
                            MAGNET += 1
                        
                elif MAGNET < IRON:

                    for i in range(MAGNET, IRON + 1):
                        if i == S.find(':', i):
                            SHEET += 1
                    
                    P = K + 1 - abs(IRON - MAGNET) - SHEET
                    
                    if P > 0:
                        ANS += 1
                        MAGNET += 1
                        IRON += 1
                        SHEET = 0

                    else:
                        if MAGNET < IRON:
                            MAGNET += 1
                        else:
                            IRON += 1

            elif IRON == S.find('X', IRON):
                MAGNET = IRON
                MAGNET += 1 
                IRON += 1
            
            else:
                IRON += 1
                
        elif MAGNET == S.find('X', MAGNET):
            IRON = MAGNET
            MAGNET += 1 
            IRON += 1
            
        else:
            MAGNET += 1

    print(ANS)