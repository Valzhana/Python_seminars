# Task_1
# Напишите программу вычисления арифметического выражения, заданного строкой.
# Используйте операции '+', '-', '/', '*'.
# Приоритет операций стандартный.

num = '7 + 2 * 10 / 5'
num = num.split()
print(num)
while len(num) > 1:
    while '*' in num or '/' in num:
        if num.count('*') > 0 and num.count('/') > 0:
            if num.index('/') > num.index('*'):
                num[num.index('*') - 1] = int(num[num.index('*') - 1]) * int(num[num.index('*') + 1])
                num.pop(num.index('*') + 1)
                num.pop(num.index('*'))
            else:
                num[num.index('/') - 1] = int(num[num.index('/') - 1]) / int(num[num.index('/') + 1])
                num.pop(num.index('/') + 1)
                num.pop(num.index('/'))
        else:
            if '*' in num:
                num[num.index('*') - 1] = int(num[num.index('*') - 1]) * int(num[num.index('*') + 1])
                num.pop(num.index('*') + 1)
                num.pop(num.index('*'))
            else:
                num[num.index('/') - 1] = int(num[num.index('/') - 1]) / int(num[num.index('/') + 1])
                num.pop(num.index('/') + 1)
                num.pop(num.index('/'))
    while '+' in num or '-' in num:
        if num.count('-') > 0 and num.count('+') > 0:
            num[num.index('-') - 1] = int(num[num.index('-') - 1]) - int(num[num.index('-') +1])
            num.pop(num.index('-') + 1)
            num.pop(num.index('-'))
            num[num.index('+') - 1] = int(num[num.index('+') - 1]) + int(num[num.index('+') + 1])
            num.pop(num.index('+') + 1)
            num.pop(num.index('+'))
        else:
            if '-' in num:
                num[num.index('-') - 1] = int(num[num.index('-') - 1]) - int(num[num.index('-') + 1])
                num.pop(num.index('-') + 1)
                num.pop(num.index('-'))
            else:
                num[num.index('+') - 1] = int(num[num.index('+') - 1]) + int(num[num.index('+') + 1])
                num.pop(num.index('+') + 1)
                num.pop(num.index('+'))
print(num)
