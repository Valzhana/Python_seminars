#Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

str1 = input('Enter the first string: ')
str2 = input('Enter the second string:')
str1_arr = str1.split()
count = 0
for i in str1_arr:
    if i.lower() == str2.lower():
        count += 1
print(count)

str1 = input('Enter the first string: ')
str2 = input('Enter the second string:')
print(str1.count(str2))