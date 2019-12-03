import math
#2
lst = [1.23, 1.24, 9.56667, 9.56666]
print('Задание 2: ', max(lst))
#3
x = 1.23
y = 2.34
z = 3.56
print('Задание 3: ', max((x + y + z), (x * y * z)))
#4
x = 2.325
y = 3.2345
z = 4.856
print('Задание 4: ', min(((x + y + z)/2, x * y * z))**2 + 1)
#5
x = 1.234
y = -2.223
z = 3.567
print('Задание 5: ', end='')
if x > 0: print(x * x, end=' ')
if y > 0: print(y * y, end=' ')
if z > 0: print(z * z)
#6
k = 1
l = 0
if k != l:
    k = l = max(k, l)
else:
    k = l = 0
print('Задание 6: ', k, l)
#7
k = 0
l = 1
m = 3
if k != l or l != m:
    k *= k
    l *= l
    m *= m
else:
    k = l = m = 0
print('Задание 7: ', k, l, m)

#8
x = 23
e = 2.71828
x1 = abs(x) + 1
x2 = (1 + x**2)**x
lst = sorted([e**x, x1, x2])
print('Задание 8: ', round(lst[0], 3), round(lst[1], 3), round(lst[2], 3))
#9
x = 90
lst = sorted([x/x**2 + 1, 1 + math.sin(x), abs(1 + x)/math.cos(x)])
print('Задание 9: ', round(lst[0], 3), round(lst[1], 3), round(lst[2], 3))
#14
x = 1
y = 2
z = 3
print('Задание 14: ')
if (x > 5) and (x < 13) and (x % 2 == 0):
    print(x)

if (y > 5) and (y < 13) and (y % 2 == 0):
    print(y)

if (z > 5) and (z < 13) and (z% 2 == 0):
    print(z)

#15
print('Задание 15: ')
if (x > -20) and (x < -8):
    print(x)

if (y > -20) and (y < -8):
    print(y)

if (z > -20) and (z < -8):
    print(z)

#16
a = 1
b = 2
c = 3
d = 4
if a * b >= c * d:
    print('Задание 16: ', a * b * c * d)
else:
    print('Задание 16: ', a * a + b * b + c * c + d * d)

#17
a = 1
b = 2
c = 3
d = 4
print('Задание 17')
if a >= 0 and a % 2 == 0:
    print(a**0.5)

if b >= 0 and b % 2 == 0:
    print(b**0.5)

if c >= 0 and c % 2 == 0:
    print(c**0.5)

if d >= 0 and d % 2 == 0:
    print(d**0.5)

#часть 2
#1
x = [2, 2, 3, 3, 6, 22, 111, 111]
inp = 5
razn = max(x)
numb = 0
for i in range(len(x)):
    if razn > inp - x[i]:
        razn = inp - x[i]
        numb = i
print('Часть 2, номер 1: ', numb - 1)
#2
xmax = max(x)
xmin = min(x)
#x = [str(x[j]) for j in x]
#for i in range(len(x)):
 #   x[i] = str(x[i])
#y = ' '.join(x)
y = x.count(xmax)
print('Часть 2, номер 2: ', y)
#3
y = x.count(xmin)
print('Часть 2, номер 3: ', y)

#часть 3
#1
x = 123456
lst = []
for i in range(len(str(x)) - 1, -1, -1):
    lst.append(str(x)[i])
lst = ''.join(lst)
print('Часть 3, задание 1', lst)
#
x = 277
print(bin(x))