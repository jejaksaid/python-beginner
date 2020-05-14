#input data user

#data input pasti string
data = input("input data: ")
print("data = ", data, "type=", type(data))

#jika ingin int, kita casting data lagi :)

number = int(input("input data: "))
print("data = ", number, "type =", type(number))

number = float(input("input data :"))
print("data = ", number, "type=", type(number))

#boolean
biner = bool(int(input("input data boolean:")))
print("data =", biner, "type=", type(biner))