# BeautifulSoup 모듈을 이용한 영화 순위 가져오기

# BeautifulSoup 이용한 단순 하이퍼 링크 가져오기
from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('http://www.naver.com/')   # response 는 단순 변수
soup = BeautifulSoup(response, 'html.parser') # html.parser 추출기
for anchor in soup.find_all('a'):
    print(anchor.get('href', '/'))


# BeautifulSoup 를 이용한 영화박스오피스 가져오기
# from bs4 import BeautifulSoup
# from urllib.request import urlopen

# response = urlopen('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%98%81%ED%99%94+%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4')

# soup = BeautifulSoup(response, 'html.parser')

# # txt 파일에 저장하기
# i = 1
# f = open("movie_rank.txt", 'w', encoding='utf-8')
# for anchor in soup.select("div.title_box"):
#     data = str(i) + "위 :" + anchor.get_text() + "\n"
#     i += 1
#     f.write(data)
# f.close()

# # 터미널에 직접 출력하기
# i = 1
# for anchor in soup.select("div.title_box"):
#     data = str(i) + "위 :" + anchor.get_text()
#     if i > 10:
#         break
#     i += 1
#     print(data)