print('============function')
#didalam function bisa ada string, boolean, float, integer
# #JANGAN LUPA :
# 1. penamaan nama():
# 2. pemanggilan fungsi dibawah


def hi_there(name, age, work, heigh):
    print("Hello " + name + " you are " + str(age)
          + " and you " + str(bool(work)) + " you are " + str(float(heigh)))

# print("top")
hi_there("said", 22, True, 170 )
hi_there("ganteng", 24, False, 180 )
# print("bottom")