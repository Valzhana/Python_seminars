lst = [2, 7, 5, 3, -4]
print(lst, '\n')
new_lst = []
half_len = len(lst) // 2
for i in range(0, half_len):
    if len(lst) % 2 == 0:
        new_lst.append(lst[i] * lst[-i-1])
        print(new_lst)
    else:
        result = str(new_lst).join(str((lst[half_len] ** 2)))
        print(result)
