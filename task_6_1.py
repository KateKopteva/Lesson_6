from random import randint
n, m, a, b = int(input()), int(input()), int(input()), int(input())
maxi = a
mini = b
total = 0
sum_r = []
matr = []
for i in range(n):
    l = []
    for j in range(m):
        r = randint(a, b)
        l.append(r)
        if r > maxi:
            maxi = r
        if r < mini:
            mini = r
        total += r
    matr.append(l)
for i in range(len(matr)):
    sum_r.append(sum(matr[i]))
print(matr)
print(maxi)
print(mini)
print(total)
print(sum_r.index(max(sum_r)))
