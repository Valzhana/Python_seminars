

num = int(input('Enter the number: '))
sum = 0
dict = {}
for i in range(1, num + 1):
    dict[i] = round((1 + (1/i)) ** i, 2)
    sum += dict[i]
print(dict)
print(sum)




