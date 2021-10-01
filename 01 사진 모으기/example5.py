import requests
import json
import os

# 카카오 이미지 검색 OpenAPI 사용해서 이미지 검색 후 파일 저장하기 (사용자에게 검색어, 갯수 입력받는 버전)

search_keyword = input("이미지를 검색하세요: ")
save_count = int(input("저장할 이미지 갯수를 입력하세요: "))


# 함수 : 이미지 url을 통해 파일 저장
def save_image(image_url, file_name):
    # verify = False : SSL 오류 해결
    img_response = requests.get(image_url, verify=False)

    if img_response.status_code == 200:
        # 성공
        with open(file_name, "wb") as fp:
            fp.write(img_response.content)


# 이미지 검색
url = "https://dapi.kakao.com/v2/search/image"
headers = {"Authorization": "KakaoAK 07161ceffeaceb948067e2c3f40ccdf3"}
data = {"query": search_keyword}

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
        # 이미지 url 출력
        print(f"[{count+1}th] image_url = ", image_info['image_url'])


        # 저장할 이미지 파일 이름 설정
        count = count + 1
        file_name = "test_%d.jpg" % (count)

        # 파일 저장
        save_path = "img/"

        try:
            if not (os.path.isdir(save_path)):
                os.makedirs(os.path.join(save_path))
        except OSError:
            print("디렉터리 생성 실패")

        save_image(image_info['image_url'], save_path + file_name)
        if count == save_count:
            break
