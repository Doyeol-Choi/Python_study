# 현재의 날짜, 시간 출력하기

# 날짜/시간 모듈 가져오기

import datetime

# 현재의 날짜 시간을 구합니다.

now = datetime.datetime.now()

# 출력하기
'''
print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,   # 년
    now.month,  # 월
    now.day,    # 일
    now.hour,   # 시간
    now.minute, # 분
    now.second  # 초
    ))
'''
# print(now)
# print(type(now))

if now.hour < 12:
    print(f"현재 시각은 {now.hour}시로 오전입니다!")
else:
    print(f"현재 시각은 {now.hour}시로 오후입니다!")
    
if now.month in [3,4,5]:
    print(f"이번달은 {now.month}월로 봄입니다!")
elif now.month in [6,7,8]:
    print(f"이번달은 {now.month}월로 여름입니다!")
elif now.month in [9,10,11]:
    print(f"이번달은 {now.month}월로 가을입니다!")
else:
    print(f"이번달은 {now.month}월로 겨울입니다!")
    
# print("{0:<2}".format('년'), end=" : ")
# print("{0:>4}년".format(now.year))
# print("{0:<2}".format('월'), end=" : ")
# print("{0:>4}월".format(now.month))
# print("{0:<2}".format('일'), end=" : ")
# print("{0:>4}일".format(now.day))
# print("{0:<2}".format('시'), end=" : ")
# print("{0:>4}시".format(now.hour))
# print("{0:<2}".format('분'), end=" : ")
# print("{0:>4}분".format(now.minute))
# print("{0:<2}".format('초'), end=" : ")
# print("{0:>4}초".format(now.second))

print('''
년 : {0:>4}년
월 : {1:>4}월
일 : {2:>4}일
시 : {3:>4}시
분 : {4:>4}분
초 : {5:>4}초
'''.format(now.year, now.month, now.day, now.hour, now.minute, now.second))
