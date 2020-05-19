print('===LEBIH BESAR (>) ===')
x = 5.9
y = 3

result = x > 7
print(x,'>',7,'=', result)

print('===lebih kecil (<)===')
result = y < 2
print(y,'<', 1,'=', result)

print('===lebih dari sama dengan (>=)===')
result = x >= 6
print(x, '>=', 6, result)

print('===kurang dari sama dengan (<=)===')
result = y <= 3
print(y, '<=', 3, result)

print('=== sama dengan (==)===')
result = x == 6
print(x, '==', 6, result)

print('====tidak sama dengan (!=)===')
result = y != 3
print(y,'!=', 3,result)

print('=== object identity(is)===')
x = 5
y = 5
print('x id =', hex(id(x)) )
print('y id =', hex(id(y)) )
result = x is 5
print("x is 5=", result)

print('===object identity(is not)===')
x = 4
y = 5
print('x id = ', hex(id(x)))
print('x id = ', hex(id(y)))
result = y is not 5
print('x is not 5', result)















