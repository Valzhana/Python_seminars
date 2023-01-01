
N = int(input('Enter N: '))
lst = []
for i in range(-abs(N), abs(N) + 1, 1):
    lst.append(i)
print(lst)

result = 1
path = 'file.txt'
with open(path, 'r') as data:
    for e in data:
        result *= lst[int(e)]
    print(result)


