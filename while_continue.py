# a = 0
# while a < 10:
#     a = a + 1
#     if a % 2 == 0:
#         continue    # continue를 만나면 다음 한 줄 처리를 skip한다.
#     print(a)

    

# 자연수 1부터 10까지 짝수의 합계를 출력하라.
# sum : 짝수의 합계 누적변수
# i : 증가 변수

i, sum = 0, 0
while i <= 10:
    i += 1
    if i % 2 == 1:  # 홀수 일때는 continue를 만나서 다음문장인 sum을 누적하지 않는다. while문 처음으로 돌아감.
        continue
    sum += i
print(sum)