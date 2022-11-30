
num = int(input('Enter the number: '))
sum = 0
while num > 0:
    num1 = num % 10
    sum += num1
    num //= 10
print(sum)


num = float(input('Enter the number: '))
while num % 1 != 0:
    num *= 10
sum = 0
while num > 0:
    num1 = num % 10
    sum += num1
    num //= 10
print(int(sum))
