import random as r

# 더하기
def addition():
    a = r.randint(1,100)
    b = r.randint(1,100)
    ans = a + b
    u_ans = int(input(f'{a} + {b} = '))
    return ans, u_ans
    
# 빼기
def subtraction():
    while True:
        a = r.randint(1,100)
        b = r.randint(1,100)
        if a < b:
            continue
        else:
            ans = a - b
            u_ans = int(input(f'{a} - {b} = '))
            break
    return ans, u_ans

# 곱하기
def multiply():
    a = r.randint(1,20)
    b = r.randint(1,10)
    ans = a * b
    u_ans = int(input(f'{a} × {b} = '))
    return ans, u_ans

# 나누기
def division():
    while True:
        a = r.randint(1,50)
        b = r.randint(1,50)
        if (a % b == 0) and (a > b):
            ans = a / b
            u_ans = int(input(f'{a} ÷ {b} = '))
            break
        else:
            continue
    return ans, u_ans

# 정답확인
def check(ans, u_ans):
    if ans == u_ans:
        print('정답입니다.')
    else:
        print(f'틀렸습니다. 정답은 {ans:.0f} 입니다.')
    return False
    
# 동작      
def main():
    togle = True
    while togle:
        print('''
1) Addition
2) Subtraction
3) Multiply
4) Division
''')
        cho = input('Enter 1 ~ 4 : ')
        if cho == '1':
            ans, u_ans = addition()
        elif cho == '2':
            ans, u_ans = subtraction()
        elif cho == '3':
            ans, u_ans = multiply()
        elif cho == '4':
            ans, u_ans = division()
        else:
            print("유효하지 않습니다. 다시입력해주세요.")
            continue
        togle = check(ans,u_ans)
            
main()

# check() 함수를 사칙연산 안으로 넣어서 실행하는 법도 있다.
# 사칙연산에서의 답과 유저값을 튜플로 넣어서 뽑아오면 main()에서 while을 굳이 안쓰고 할 수 있다.