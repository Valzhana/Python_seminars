num = input('Enter the number: ')
sum_digit = 0
for e in str(num):
    if e != '.':
        sum_digit += int(e)
print(sum_digit)
