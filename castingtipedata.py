#merubah dari satu tipe ke tipe lain
#tipe data = int, float, str, bool
print("====INTEGER====")
data_int = 0
print("data = ", data_int, type(data_int))

data_float = float(data_int)
print("data2 = ", data_float, type(data_float))
data_str = str (data_int)
print("data3 = ", data_str, type(data_str))
data_bool = bool (data_int)
print("data4 = ", data_bool, type(data_bool))

print("====FLOAT====")
data_float = 10
print("data = ", data_float, type(data_float))

data_int  = int(data_float) #akan dibulatkan kebawah
data_str  = str(data_float)
data_bool = bool(data_float)
print("data = ", data_int, type(data_int))
print("data = ", data_str, type(data_str))
print("data = ", data_bool, type(data_bool))

print("====STRING====")
data_str = "10"
print("data = ", data_str, type(data_str))

data_bool = bool(data_str) #false jika nilai kosong
data_int = int(data_str) #harus angka
data_float = float(data_str) #harus angka
print("data = ", data_bool, type(data_bool) )
print("data = ", data_int, type(data_int))
print("data = ", data_float,type(data_float) )

print("====BOOLEAN====")
data_bool = False;
print("data = ", data_bool, type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)

print("data = ", data_int, type(data_int))
print("data = ", data_str, type(data_str))
print("data = ", data_float, type(data_float))