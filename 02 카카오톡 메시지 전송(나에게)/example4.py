import json
import requests
import kakao_def

# load token
tokens = kakao_def.load_tokens(kakao_def.KAKAO_TOKEN_FILENAME)

# 리스트 메시지 url
url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

# request parameter 설정, Bearer 옆 공백 넣어야 오류 안남
headers = {"Authorization": "Bearer " + tokens['access_token']}

template = {
    "object_type" : "list",
    "header_title" : "초밥 사진",
    "header_link" : {"web_url" : "www.naver.com", "mobile_web_url" : "www.naver.com"},
    "contents" : [
        {
            "title" : "1. 광어 초밥",
            "description" : "광어 존맛",
            "image_url" : "https://search1.kakaocdn.net/argon/0x200_85_hr/8x5qcdbcQwi",
            "image_width" : 50,
            "image_height" : 50,
            "link" : {"web_url" : "www.naver.com", "mobile_web_url" : "www.naver.com"}
        },
        {
            "title": "2. 참치 초밥",
            "description": "참치 존맛",
            "image_url": "https://search2.kakaocdn.net/argon/0x200_85_hr/IjIToH1S7J1",
            "image_width": 50,
            "image_height": 50,
            "link": {"web_url": "www.naver.com", "mobile_web_url": "www.naver.com"}
        }
    ],
    "buttons" : [{
        "title" : "웹으로 기기",
        "link" : {"web_url" : "www.naver.com", "mobile_web_url" : "www.naver.com"}
    }]
}
data = {"template_object": json.dumps(template)}

# 나에게 카카오톡 메시지 보내기 요청 list 버전
response = requests.post(url, headers=headers, data=data)
print(response.status_code)

# 요청 프로세스
if response.status_code != 200:
    # 요청 실패
    print("error! because ", response.json())
else:
    # 요청 성공
    print("메시지 전송 성공")
