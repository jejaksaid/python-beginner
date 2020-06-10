import random
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=[:]{};\|,.<>/?"'

number = input('Number of password? - ')
number = int(number)

length = input('Password length? - ')
length = int(length)

for p in range(number):
    password = ' '
    for c in range(length):
        password += random.choice(chars)
    print(password)