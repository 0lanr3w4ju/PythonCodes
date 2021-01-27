# removes duplicates in a list

list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 9, 8, 7, 6, 5, 4, 4, 3, 3, 4, 5, 6, 7, 8]

list_two = []

for digit in list_one:
    if digit not in list_two:
        list_two.append(digit)

print(list_two)
