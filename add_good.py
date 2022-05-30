# import random
# a = random.randint(10,99)
# b = random.randint(100,999)

import random as r

a = r.randint(10,99)        # import random as r 로 인해 random을 r로 써준다.
b = r.randint(100,999)

while True:
    print(f"   {a}")
    print(f"+ {b}")
    print("-----")

    c = int(input())

    if c == (a + b):
        print("정답입니다. -- 축하합니다!")
    else:
        print(f"틀렸습니다. 정답은 {a+b} 입니다.")