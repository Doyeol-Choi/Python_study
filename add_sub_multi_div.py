import random as r

# 더하기
def addition():
    a = r.randint(1,100)
    b = r.randint(1,100)
    ans = int(input(f'{a} + {b} = '))
    if ans == (a+b):
            print('정답입니다.')
    else:
        print(f'틀렸습니다. 정답은 {a+b} 입니다.')
    
# 빼기
def subtraction():
    while True:
        a = r.randint(1,100)
        b = r.randint(1,100)
        if a < b:
            continue
        else:
            ans = int(input(f'{a} - {b} = '))
            if ans == (a-b):
                print('정답입니다.')
            else:
                print(f'틀렸습니다. 정답은 {a-b} 입니다.')
            break

# 곱하기
def multiply():
    a = r.randint(1,20)
    b = r.randint(1,10)
    ans = int(input(f'{a} × {b} = '))
    if ans == (a*b):
        print('정답입니다.')
    else:
        print(f'틀렸습니다. 정답은 {a*b} 입니다.')

# 나누기
def division():
    while True:
        a = r.randint(1,50)
        b = r.randint(1,50)
        if (a % b == 0) and (a > b):
            ans = int(input(f'{a} ÷ {b} = '))
            if ans == (a/b):
                print('정답입니다.')
            else:
                print(f'틀렸습니다. 정답은 {a/b:.0f} 입니다.')
            break
        else:
            continue

# 동작      
def main():
    while True:
        print('''
1) Addition
2) Subtraction
3) Multiply
4) Division
''')
        cho = input('Enter 1 ~ 4 : ')
        if cho == '1':
            addition()
            break
        elif cho == '2':
            subtraction()
            break
        elif cho == '3':
            multiply()
            break
        elif cho == '4':
            division()
            break
        else:
            print("유효하지 않습니다. 다시입력해주세요.")
            
main()
    