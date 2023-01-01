# Найти НОК и НОД двух

number1 = int(input('Enter the number: '))
number2 = int(input('Enter the number: '))
new_lst = []
new_lst1 = []


def f(lst, number):
    factor = 2
    while number > 1:
        if number % factor == 0:
            lst.append(factor)
            number //= factor
        else:
            factor += 1


f(new_lst, number1)
f(new_lst1, number2)
print(set(new_lst))
print(set(new_lst1))
nod_find = set(new_lst).intersection(set(new_lst1))
nod = 1
for i in nod_find:
    nod *= i
nok = number1 * number2 // nod
print(nod)
print(nok)
