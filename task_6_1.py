from random import randint
n, m, a, b = int(input()), int(input()), int(input()), int(input()),
matr = []
for i in range(n):
    l = []
    for j in range(m):
        l.append(randint(a,b))
    matr.append(l)
