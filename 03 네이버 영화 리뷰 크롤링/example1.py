from bs4 import BeautifulSoup
import lxml

# 파이썬 웹 크롤러 구현 연습

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; 
and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'lxml')

# soup 객체 - body 태그 하위 태그인 p 태그 출력
print("soup.body.p의 결과: ", soup.body.p)
# <p class="title"><b>The Dormouse's story</b></p>

# soup 객체 - a 태그의 속성 출력 (딕셔너리 형태)
print("soup.a['href']의 결과: ", soup.a['href'])
# http://example.com/elsie

# soup 객체 - title 태그 이름 출력
print("soup.title.name의 결과: ", soup.title.name)
# title

# soup 객체 - title 태그 문자열 출력
print("soup.title.string의 결과: ", soup.title.string)
# The Dormouse's story

# soup 객체 - 태그의 자식들을 리스트로 반환 출력
print("soup.contents의 결과: ", soup.contents)
# [<html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters;
# and their names were
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# </body></html>]

# find()
print("soup.find()의 결과: ", soup.find('a', class_='sister'))
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

# find_all()
print("soup.find_all()의 결과: ", soup.find_all('a', limit=2))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]