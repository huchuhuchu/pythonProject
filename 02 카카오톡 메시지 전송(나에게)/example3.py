import json
import requests
import kakao_def

tokens = kakao_def.load_tokens(kakao_def.KAKAO_TOKEN_FILENAME)

# 텍스트 메시지 url
url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

# request parameter 설정, Bearer 옆 공백 넣어야 오류 안남
headers = {"Authorization": "Bearer " + tokens['access_token']}

data = {
    "template_object": json.dumps({
        "object_type": "text",
        "text": "Hello, world!@sss",
        "link": {"web_url": "www.naver.com"}
    })
}

# 나에게 카카오톡 메시지 보내기 요청 text 버전
response = requests.post(url, headers=headers, data=data)
print(response.status_code)

# 요청 프로세스
if response.status_code != 200:
    # 요청 실패
    print("error! because ", response.json())
else:
    # 요청 성공
    print("메시지 전송 성공")
