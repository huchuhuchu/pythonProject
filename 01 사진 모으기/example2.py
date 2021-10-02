import requests
import json

# 카카오 이미지 검색 OpenAPI 사용해서 이미지가 있는 URL 출력하기

# search img
url = "https://dapi.kakao.com/v2/search/image"
headers = {
    "Authorization" : "KakaoAK key"
}
data = {
    "query" : "bmo"
}

# 서버로 이미지 검색 요청
response = requests.post(url, headers=headers, data=data)

# 요청
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