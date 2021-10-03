# 네이버 영화 리뷰 페이지 크롤링
# 설계 : 총 리뷰 갯수 확인, (1) 제목만, (2) 내용만, (3) 제목과 내용, (4) 풀리뷰
import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/bi/mi/review.naver?code=191633"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

# 리뷰 count
review = soup.find('span', class_="cnt")
cnt = review.find('em').getText()

ul = soup.find('ul', class_="rvw_list_area")
lis = ul.find_all('li')
cont = ul

print(f"총 {cnt} 건의 리뷰")

count = 0
for li in lis:
    count += 1
    print(f"({count})")
    print(li.a.string)
    print(li.p.string)
    print("-----")

