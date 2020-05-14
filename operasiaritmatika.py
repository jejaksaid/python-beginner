#operasi aritmatika

a = 14
b = 3
#pertambahan
result = a + b
print('pertambahan', a, '+',b, '=', result)

#perkalian

result = a * b
print('perkalian',a, '*', b , '=', result)

#pembagian

result = a / b
print('pembagian',a, '/', b, '=', result)

#eksponen / pangkat
result = a ** b
print('eksponen/perpangkatan',a, '**', b,'=', result)

#modulus
result = a % b
print('modulus (sisa hasil bagi)',a, '%', b,'=', result)

#floor division
result = a // b
print('floor division(pembulatan kebawah)',a, '//', b, '=', result)
print("========================")

#prioritas operasi, operational precedence

x = 4
y = 50
z = 10.2
result = x * y + z // y ** z - (-x % y)
print('prioritas operasi',x, '*', z, '*', y, '+', z, '//', y, '**',z, '-', x,'%',y, '=', result)
'''
#1. ()
#2. eksponen **
#3. perkalian dll *, /, %, //
#4. pertambahan dan pengurangan +, -
'''