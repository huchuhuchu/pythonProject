import requests
import json

# 카카오 이미지 검색 OpenAPI 사용해서 이미지 검색 후 파일 저장하기

# 함수 : 이미지 url을 통해 file_name 파일로 저장
def save_image(image_url, file_name):
    img_response = requests.get(image_url)

    if img_response.status_code == 200:
        # 성공
        with open(file_name, "wb") as fp:
            fp.write(img_response.content)

# 이미지 검색
url = "https://dapi.kakao.com/v2/search/image"
headers = {"Authorization" : "KakaoAK 07161ceffeaceb948067e2c3f40ccdf3"}
data = {"query" : "bmo"}

# 서버로 이미지 검색 요청
response = requests.post(url, headers=headers, data=data)

# 요청 프로세스
if response.status_code != 200:
    # fail
    print("error! because - ", response.json())
else:
    # success
    count = 0
    for image_info in response.json()['documents']:
        print(f"[{count}th] image_url = ", image_info['image_url'])

        # set image file name
        count = count+1
        file_name = "test_%d.jpg" %(count)

        # save image
        save_image(image_info['image_url'], file_name)