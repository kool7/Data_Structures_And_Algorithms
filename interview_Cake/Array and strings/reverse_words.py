data = []

while True:
    char = str(input())
    if char == "":
        break
    data.append(char)

def reverse_words(data:list):

    data = data[::-1]

    string = ''

    for stng in data:
        string += stng

    return string

print(reverse_words(data))