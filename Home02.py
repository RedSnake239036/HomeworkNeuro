
#1
x = 0.1
print('задание  1', x > -1 and x < 1)
#2
x = 0.1
print('задание  2', x > 0 and x < 1)
#3
x = 0.1
print('задание  3', x < 0 and x > 1)
#4
x = 0.1
print('задание  4', 2 < x < 5 or -1 < x < 1)
#5
x = 0.1
print('задание  5', (x < 2) or (x > 5) and (-1 > x) or (x > 1))
#6
x = 1
y = 2
z = 3
print('задание  6', x == y == z)
#7
x = 1
y = 2
z = 3
print('задание  7', x == y != z or x == z != y or z == y != z)
#8
p = 8
q = 2
print('задание  8', not(p % q))
#9
a = 1
b = 2
c = -1
print('задание  9', b**2 == 4 * a * c)
#10
a = 3
b = 4
c = 5
print('задание 10', a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2)
#11
a = 3
b = 4
c = 5
print('задание 11', a**2 + b**2 > c**2 or a**2 + c**2 > b**2 or c**2 + b**2 > a**2)
#12
print('задание 12 не сделал(')
#13
a = 3
b = 4
c = 5
print('задание 13', a >= b >= c or a <= b <= c)
#2.2
#1
summ = 1
summ *= int(str(x)[0]) * int(str(x)[1]) * int(str(x)[2]) * int(str(x)[3])
print('задание  1', bool(summ % 2))
#2
k = 4
print('задание  2', '5' in str(k))
#3
x = 2
print('задание  3', x*x == (int(str(x)[0]) + int(str(x)[1]) + int(str(x)[2])**5))
#4
x = 234
print('задание  4', str(x)[0] == str(x)[1] or str(x)[0] == str(x)[2] or str(x)[1] == str(x)[2])
#5
x = 123.61078
print('задание  5', '0' in str(x).split('.')[1])
#6
x = 127
print('задание  6', x % int(str(x)[1]) == 0)
#7
x = 235
print('задание  7', int(str(x)[0]) % 2 == 0 and int(str(x)[1]) % 2 == 0 and int(str(x)[2]) % 2 == 0 )
#8
print('задание  8', (int(str(x)[0]) + int(str(x)[1]) + int(str(x)[2])) % 5 == 0)
#9
print('задание  9', int(str(x)[0]) == int(str(x)[-1]))
#10
print('задание 10', int(str(x)[0]) == int(str(x)[1]) == int(str(x)[2]))
#11
print('задание 11', int(str(x)[0]) > int(str(x)[-1]))
#12
print('задание 12', int(str(x)[1]) > int(str(x)[-1]) + int(str(x)[0]))
#13
print('задание 13', 7 in str(x))
#14
print('задание 14', int(str(x)[0]) + int(str(x)[1]) == int(str(x)[1]) + int(str(x)[2]))
#15
print('задание 15', x**0.5 == int(str(x)[0]) ** 2 + int(str(x)[1]) ** 2 + int(str(x)[2]) ** 2)
#16
print('задание 16', str(x)[0] != str(x)[1] != str(x)[2])
#17
print