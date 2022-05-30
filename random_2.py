import random

jaum = 'bcdfghhklmnpqrstvwxz'
moum = 'aeiouy'
sn = ""
for j in range(4):
    if j%2 == 0:
        sn += random.choice(jaum)
    else:
        sn += random.choice(moum)
print(sn)