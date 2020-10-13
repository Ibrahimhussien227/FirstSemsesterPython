lis = [1, 2, 3, 4, 5]

for i in range(len(lis)):
    print(lis[i] * lis[i])

    print([i * i for i in lis])

listta = [5, 4, 3, 6, 7, 1, 7, 1]

for a in listta:
    print(a)

b = [a ** 2 if a % 2 == 0 else a ** 3
     for a in listta]
print(b)

lista = [5, 4, 3, 6, 7, 1, 7, 1]
listb = [1, 2, 5, 1, 1]

listc = [(lista[i], listb[i])
         for i in range(min(len(lista), len(listb)))]

print(listc)
len(lista)

for i in range(min(len(listb), len(lista))):
    listc.append((lista[i], listb[i]))
    print(listc)

m = [[1] * 3, [2] * 3, [3] * 3, [4] * 3]
print(*m, sep='\n')
print('==========')

lis = [1, 2, 3, 4]
a = lis[0]
b = lis[1]
c = lis[2]

a, b, *c = lis

a = 2, 3, 4
a = (2, 3, 4)
a = [2]
a = (2 + 3,)
print(a)

a = 3
b = 5
c, *a = (b, a)
print(a, b)

lis = [['i dfdfdfd'] for x in range(10)]
print(lis)
new_m = []
for col in range(len(m[0])):
    new_row = []
    for row in range(len(m)):
        new_row.append(m[row][col])
    new_m.append(new_row)
print(*new_m, sep='\n')
print('==========')

m = [[1] * 3, [2] * 3, [3] * 3, [4] * 3]
print(*m, sep='\n')
print('==========')
new_m = list(zip(*m))
print(*new_m, sep='\n')
print('==========')


