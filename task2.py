list = [1, 4, 5, 6, 8]
max = list[0]
for i in range(1, len(list)):
    if list[i] > max:
        max = list[i]
print(f'maximum number {max}')