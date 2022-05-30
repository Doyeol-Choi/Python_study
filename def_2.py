
# def add_many(*args):    # *args 여러개의 매개변수
#     result = 0
#     for i in args:
#         result += i
#     return result

# result = add_many(1,2,3,4,5,6,7,8,9,10)    
# print(result)



# def add_mul(choice, *args):     # Ctal + H 단어 찾아 바꾸기
#     if choice == "add":
#         result = 0
#         for i in args:
#             result += i
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result *= i
#     return result

# result = add_mul('add', 1,2,3,4,5,6,7,8)
# print(result)

# result = add_mul('mul', 1,2,3,4,5,6,7,8)
# print(result)



# def say_nick(nick):
#     if nick == '바보':
#         return 0  # 아무것도 안넣거나 0을 넣으면 종료하라
#     print("나의 별명은 %s입니다." % nick)
    
# # say_nick('야호')
# say_nick('바보')



def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
        
say_myself('최도열', 32)
say_myself('이수진', 32, False)