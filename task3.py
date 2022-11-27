#Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
N = int(input('Enter number N:'))
numbers = []
for i in range(- abs(N), abs(N) + 1, 1):
    numbers.append(i)
print(numbers)


N = int(input('Enter number N:'))
for i in range(- abs(N), abs(N) + 1, 1):
    print(i, end = ' ')
