#Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

    #*Пример:*
    #- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


n = int(input('Enter n: '))
dict_n = {}
for i in range(1, n + 1):
    dict_n[i] = i * 3 + 1
print(dict_n)

n = int(input('Enter n: '))
dict_n = {i: 3 * i + 1 for i in range(1, n + 1)}
print(dict_n)