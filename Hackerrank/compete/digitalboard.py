def diff_between_vertical_and_horizontal_lines(number):
    dict_hori = {'0': 2, '1': 0, '2': 3, '3': 3, '4': 1, '5': 3, '6': 3,
                 '7': 1, '8': 3, '9': 3}
    dict_verti = {'0': 4, '1': 2, '2': 2, '3': 2, '4': 3, '5': 2, '6': 3,
                 '7': 2, '8': 4, '9': 3}

    hori_sum, verti_sum = 0, 0

    for digit in number:
        hori = dict_hori[digit]
        verti = dict_verti[digit]

        hori_sum += hori
        verti_sum += verti

    return verti_sum - hori_sum

n = int(input())

lst = []
for i in range(n):
    number = input()
    lst.append(number)

for number in lst:
    print(diff_between_vertical_and_horizontal_lines(number))