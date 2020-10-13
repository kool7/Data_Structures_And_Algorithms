# num = [10, 2, 3, 16, 3, 6, 8]

# max = num[1] - num[0]
# min = num[0]

# for i in range(1, len(num)):
#         if (num[i] - min > max):
#             max = num[i] - min

#         if (num[i] < min):
#             min = num[i]
            
# print(max)
x = int(input())  
y = int(input())
z = int(input())
n = int(input())

List = [ [i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)
if ( ( i + j + k) != n )]
print(List)

