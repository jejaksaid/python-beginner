print("==============tuples")
# 1. berbeda dengan list
# 2. tidak bisa dirubah , tapi bisa ditambah
# hanya digunakan untuk situasi tertentu
coordinates1 = (2, 3) , (4, 5)
print(coordinates1[1])

# tup=ples didalam list
coordinates2 = [(2, 3, 4, 5, 6), (1,2,3,4,5)]
print(coordinates2)
#
# perbedaan tuples dan lists
# tuple is immutable
# list is mutable
list1 = ["age", 22]
list1.insert(1, 'years old')
tuple1 = ("john", list1)
print(tuple1)