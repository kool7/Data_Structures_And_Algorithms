matDim = list(map(int, input().split()))

if( (matDim[0] > 5 and matDim[0] < 101) and (matDim[0] % 2 != 0) and (matDim[1] == matDim[0] * 3)):
    for row in range(1, matDim[0], 2):
        print((row * '.|.').center(matDim[1], '-'))
    print('WELCOME'.center(matDim[1], '-'))
    for row in range(matDim[0]-2, -1, -2):
        print((row * '.|.').center(matDim[1], '-'))
else:
    print('constraints are not satisfied')