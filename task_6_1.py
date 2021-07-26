from random import randint
n, m, a, b = int(input()), int(input()), int(input()), int(input())
maxi = a
matr = []
for i in range(n):
    l = []
    for j in range(m):
        r = randint(a, b)
        l.append(r)
        if r > maxi:
            maxi = r
    matr.append(l)
print(matr)
print(maxi)
