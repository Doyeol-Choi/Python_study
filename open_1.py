# 파일 입출력

score_file = open("score.txt", 'w', encoding="utf-8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", 'a', encoding="utf-8")   # a(append)는 추가모드
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

score_file = open("score.txt", 'r', encoding="utf-8")
print(score_file.read())
score_file.close()

score_file = open("score.txt", 'r', encoding="utf-8")
print(score_file.readline())    # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline(), end="")    # 줄바꿈 안 할 때
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

print()

# 파일이 몇 줄 인지 모를 때

score_file = open("score.txt", 'r', encoding="utf-8")
while True:
    line = score_file.readline()    # 한줄씩 읽어 오기
    if not line:
        break
    print(line, end="")
score_file.close()

# list 형태로 저장

score_file = open("score.txt", 'r', encoding="utf-8")
lines = score_file.readlines()  # 여러줄 한꺼번에 읽어 오기
for line in lines:
    print(line, end="")
    
score_file.close()
    