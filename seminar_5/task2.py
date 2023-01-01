with open('forsem_5.txt', 'r') as f:
    n = list(map(int, (f.read().split())))
    print(n)
for i in range(1, len(n)):
    if n[i] - n[i - 1] > 1:
        n.insert(i, n[i - 1] + 1)
print(n)

data = open('forsem_5.txt', 'w')
data.write(' '.join(list(map(str, n))))
data.close()
