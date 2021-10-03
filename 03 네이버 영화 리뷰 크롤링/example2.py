# https://movie.naver.com/movie/bi/mi/review.naver?code=191633
# 네이버 영화, 트롤:월드 투어 페이지의 리뷰 제목 크롤링

import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/bi/mi/review.naver?code=191633"

# html 소스를 객체로 soup 변수에 저장
res = requests.get(url)

# html 파싱
soup = BeautifulSoup(res.text, 'lxml')

# 리뷰 집합인 ul 태그 찾고 다른거 안긁어오게 클래스 명시
ul = soup.find('ul', class_="rvw_list_area")

# ul 태그 기준으로 모든 li 태그 탐색해 lis 변수에 저장 (리스트 타입)
lis = ul.find_all('li')

# 리뷰 제목 출력
count = 0
for li in lis:
    count += 1
    print(f"[{count}th] ", li.a.string)