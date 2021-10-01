import requests

# request 패키지 연습 - 웹에서 이미지 다운받기

# img url
url = "https://cdnb.artstation.com/p/assets/images/images/026/481/707/large/santiago-chavarriaga-render-bmo.jpg?1588884436"

# 서버로 url 요청
img_response = requests.get(url)

# 요청 성공
if img_response.status_code == 200:
    # 이미지 바이너리 파일 출력
    # print(img_response.content)

    print("=save img=")

    # wb = 바이너리 형식을 쓰는 모드
    with open("test.jpg", "wb") as fp:
        fp.write(img_response.content)