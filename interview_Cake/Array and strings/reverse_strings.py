# reverse string
data = []

while True:
    char = str(input())
    if char == "":
        break
    data.append(char)

print(data[::-1])

