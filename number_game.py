import random as r

def com_rand():
    ran = r.randint(1,10)
    return ran
    
def get_num():
    ans = int(input("숫자를 맞춰보세요. (1-10) : "))
    return ans

# def get_num():
#     while True:
#         ans = input("숫자를 맞춰보세요. (1-10) : ")
#         if ans in str(range(1,11)):
#             ans = int(ans)
#             break
#         else:
#             print("1-100 사이의 숫자를 입력해주세요")
#     return ans
    
def game():
    counter = 1
    ran = com_rand()
    while True:
        ans = get_num()
        if ans == ran:
            print(f"정답입니다. 입력한 숫자는 {ran}입니다.\n")
            break
        elif ans > ran:
            print("숫자가 너무 큽니다.")
        else:
            print("숫자가 너무 작습니다.")
        counter += 1
    return counter

score = []    
# start = 1
# while start <= 5:
#     print(f"{start}회차 게임", "-"*24)
#     counter = game()
#     score.append(counter)
#     start += 1
    
# aver = sum(score)/len(score)

# print(f"게임스코어는 {score}입니다.")
# print(f"평균적으로 {aver}회만에 맞추셨습니다.")

for start in range(5):
    print(f'{start+1}회차 게임 ','-'*30)
    
    score.append(game())

print(f'게임스코어는 {score} 입니다.')
print('평균적으로 {}회만에 맞추셧습니다.'.format(sum(score)/len(score)))