# 영화 리뷰 가져오기

import requests
from bs4 import BeautifulSoup

# 네이버 영화 리뷰 - 타이타닉
url = "https://movie.naver.com/movie/bi/mi/review.naver?code=18847"

# html 소스 가져오기
res = requests.get(url)

# html 파싱
soup = BeautifulSoup(res.text, 'lxml')

# 리뷰 리스트
ul = soup.find('ul', class_="rvw_list_area")    # 크롬에서 네이버영화 접속후 해당영화리뷰 소스 Ctrl + Shift + i(F12)
lis = ul.find_all('li')

# 리뷰 제목 출력
count = 0
for li in lis:
    count += 1
    print(f"[{count}th] ", li.a.string)