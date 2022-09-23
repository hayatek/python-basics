t  = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 8, 10)

l = []
for i in t:
    if i % 2 == 0:
        l.append(i)
print(l)
l = [i for i in t if i % 2 ==0]
print(l)

l = []
for i in t:
    for j in t2:
        l.append(i * j)

print(l)

l = [i * j for i in t for j in t2]

print(l)