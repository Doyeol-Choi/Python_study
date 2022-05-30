# beautifulsoup 모듈로 오늘 날씨 가져오기

from urllib import request
from bs4 import BeautifulSoup
import datetime

now = datetime.datetime.now()

# urlopen() 함수로 기상청의 날씨를 읽는다.

target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
# 링크 한줄 코드임
# 기상청 홈페이지(https://www.weather.go.kr/w/index.do)에 가서 전국중기예보, 링크코드를 하단 RSS 방식으로 링크전환 후 복사 붙여넣기
soup = BeautifulSoup(target, "html.parser")

print(f'{now.year}년 {now.month}월 {now.day}일\n')
for location in soup.select("location"):
    print("날짜:",location.select_one("tmEf").string)
    print("도시:",location.select_one("city").string)
    print("날씨:",location.select_one("wf").string)
    print("최저기온:",location.select_one("tmn").string)
    print("최고기온:",location.select_one("tmx").string)
    print()