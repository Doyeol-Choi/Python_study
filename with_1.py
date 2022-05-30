# with

with open("study.txt", "w", encoding="utf-8") as study_file:    # r : 쓰기모드    
    study_file.write("파이썬을 열심히 공부하고 있어요") # encoding="utf-8" 한글인코딩
    
with open("study.txt", "r", encoding="utf-8") as study_file:    # r : 읽기 모드
    print(study_file.read())
    
# 미션 : 나는 회사에서 매주 1회 작성해야 하는 보고서가 있다.
# 보고서의 형식은 아래와 같다.

# - x 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 : 

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
# 조건 : 파일명은 '1주차.txt', '2주차.txt', '3주차.txt'

# for i in range(1,51):
#     with open(str(i) + "주차.txt", 'w', encoding="utf-8") as report_file:
#         report_file.write('- {0} 주차 주간보고 -'.format(i))
#         report_file.write('\n부서 : ')  # write는 이어서 출력되기 때문에 개행해준다
#         report_file.write('\n이름 : ')
#         report_file.write('\n업무 요약 : ')