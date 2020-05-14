#input data user

data1 = input("enter your name:")
print("Hello "+ data1 + "!" , type(data1))
data2 = input("your origin: ")
print("im from " + data2)
data3 = input("what you like: ")
print("i love " + data3)
#jika ingin int, kita casting data lagi :)
#input data user

#data input pasti string
data = input("enter your name:")
print("Hello ", data, "!")

#jika ingin int, kita casting data lagi :)

number = int(input("input data: "))
print("data = ", number, "type =", type(number))

number = float(input("input data :"))
print("data = ", number, "type=", type(number))

#boolean
biner = bool(int(input("input data boolean:")))
print("data =", biner, "type=", type(biner))