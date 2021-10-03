import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/bi/mi/review.naver?code=191633"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

# 리뷰 페이징 count
paging = soup.find('div', class_="paging")
paging_cnt = paging.find_all('a')
print(paging_cnt)

count = 0
paging_list = []
for a in paging_cnt:
    count += 1
    paging_list = a.span.string
    print(type(paging_list))

print(len(paging_list))

# review_list = []
# for page in range(1,11):
#     url = f"https://movie.naver.com/movie/bi/mi/review.naver?code=191633&page="{page}
