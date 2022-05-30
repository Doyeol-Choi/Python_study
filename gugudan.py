# 구구단 실행하기

def dan():
    while True:
        n = int(input("출력할 단 입력(종료 : 0) : "))
        print()
        if n == 0:
            break
        else:
            for m in range(1,10,1):       # range(1,10,1) : 1부터 10미만까지 1씩 증가
                print("{0} x {1} = {2}".format(n, m, n*m)) # , end = " " 한 줄 입력시
        print()        
dan()



x = 1
list = []
while x != 0:   # 0 이 입력되면 while 정지 후 출력
    x = int(input("출력할 단 입력(종료 : 0) : "))
    if x != 0:
        list.append(x)

print("\n출력할 구구단 : ", list, "\n")
for i in list:
    y=0
    while y <= 8:
        y += 1
        print(i,"x",y,"=",i*y)
    print()