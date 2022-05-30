import random

   
# def low_high_range():
#     low = int(input("낮은 숫자를 입력하세요 : "))
#     high = int(input("높은 숫자를 입력하세요 : "))
#     comp_num = random.randint(low, high)
#     return comp_num

def low_high_range():
    error = True
    while error:
        low = int(input("낮은 숫자를 입력하세요 : "))
        high = int(input("높은 숫자를 입력하세요 : "))
        if high <= low:
            print("높은 숫자를 낮은 숫자보다 높게 다시 입력해주세요.")
        else:
            error=False
    comp_num = random.randint(low, high)
    return comp_num
    
def user_ask():
    ask = int(input("당신이 생각하는 숫자는 무엇인가요?...... : "))
    return ask

def check(ask, comp_num):
    if ask == comp_num:
        print("정확합니다. 게임에 승리하였습니다.")
        state = False
    elif ask > comp_num:
        print("\n너무 높은 숫자입니다.")
        state = True
    else:
        print("\n너무 낮은 숫자입니다.")
        state = True
    return state

def main():
    state = True
    comp_num = low_high_range()
    while state:
        ask = user_ask()
        state = check(ask, comp_num)


# def check(ask, comp_num):
#     if ask == comp_num:
#         return True
#     else:
#         return False
    
# def main():
#     comp_num = low_high_range()
#     state = True
#     while state:
#         user_ask_int = user_ask()
#         if check(user_ask_int, comp_num):
#             state = False                 # toggle 상태전환키
#             print("정확합니다. 게임에 승리하였습니다.")
#         else:
#             if user_ask_int > comp_num:
#                 print("\n너무 높은 숫자입니다.")
#             elif user_ask_int < comp_num:
#                 print("\n너무 낮은 숫자입니다.")
            
            
main()