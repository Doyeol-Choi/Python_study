# Exception 예외처리

# try:    # try ~ except 는 셋트
#     number = int(input("반지름 정수 입력: "))
#     print("원의 반지름: ", number)
#     print("원의 둘레: ", 2 * 3.14 * number)
#     print("원의 넓이: ", 3.14 * number * number)
    
# except Exception as exception:  # except Exception as 까진 예약어
#     if type(exception) == ValueError:    # 반지름을 정수가 아닌 데이터를 입력했을때
#         print("예외가 발생하였습니다.")
#         print("입력값에 문제가 있습니다.")
#         print("숫자로 다시 입력해주세요.")
        
# print()

try:
    a = [125, 152, 51, 68, 99]
    number = int(input("정수 입력(0~4까지 입력하세요)> "))
    print(a[number])
    b = 4 / 0
    print(b)
    
except ValueError as exception:             # ValueError : 입력값이 숫자값이 아닐때
    print("입력값의 문제가 있습니다.")
except IndexError as exception:             # IndexError : 리스트의 인덱싱 범위를 벗어날때
    print("0~4까지 입력해주세요.")
except ZeroDivisionError as exception:      # ZeroDivisionError : 0으로 잘 못 나눌때
    print("0으로 나눌수 없습니다.")
except Exception as exception:              # Exception : 위에 나온 예외 이외의 에러일때
    print("알 수 없는 예외가 발생했습니다.")    # Ctrl + Z 와 같은것을 눌렀을때 출력됨