# Найдите корни квадратного уравнения: ax^2 + bx + c = 0
# a, b, c = int(input()), int(input()), int(input())
num = '- 4 * x^2 + 3 * x - 8 = 0'
new_num = num.split()
num1 = []
for i in new_num:
    if i.isdigit() or i == '-':
        num1.append(i)
    if i == '=':
        break

i = 0
while num1.count('-') != 0:
    if num1[i] == '-':
        num1[i] += num1[i + 1]
        num1.pop(i + 1)
    i += 1
print(num1)
a, b, c = int(num1[0]), int(num1[1]), int(num1[2])

d = b ** 2 - 4 * a * c
if d < 0:
    print('no roots')
if d == 0:
    print(-b / (2 * a))
if d > 0:
    print(round((-b + d ** 0.5) / 2 ** a), 2)
    print(round((-b - d ** 0.5) / 2 ** a), 2)
