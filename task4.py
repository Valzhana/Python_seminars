#Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
num = float(input('Enter the number:'))
print(int((num % 1) * 10))


num = input('Enter the number:')
for i in range (len(num)):
    if num[i] == '.':
        print(num[i + 1])
        break