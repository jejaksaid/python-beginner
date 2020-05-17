# if statement and conditions
#boolean sederhana dengan if else
#booelan 1 = True , 0 = False
print("================or condition")
is_num = False
is_num_big = False
# if is_num:
#     print("you are right")
if is_num or is_num_big:
    print('you are right!')
else:
    print("you are wrong :)")


print("================and condition")
is_num = True
is_big = True
if is_big and is_num:
    print("right")
else:
    print("wrong")

print("================and not condition")

is_num  = False
is_num_big = False

if is_num and is_num_big:
    print("right")
elif is_num and not(is_num_big):
    print("number but small number")
elif not(is_num) and (is_num_big):
    print("not numb but big")
else:
    print("not number and not big")