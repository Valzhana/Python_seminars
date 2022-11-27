#Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

a = int(input('Enter number a:'))
b = int(input('Enter number b:'))
print(a == b**2 or b == a**2)


a = int(input('Enter number a:'))
b = int(input('Enter number b:'))
if a == b**2:
    print(f'{a} is the square of {b}')
elif b == a**2:
    print(f'{b} is the square of {a}')
else:
    print('There are no squares')
