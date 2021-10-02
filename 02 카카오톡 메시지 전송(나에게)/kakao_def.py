import json
import requests
import datetime
import os

# 카카오 토큰을 저장할 파일 명
KAKAO_TOKEN_FILENAME = "kakao_token.json"

# 함수 : json 형식의 토큰 파일 저장 프로세스
def save_tokens(filename, tokens):
    with open(filename, "w") as fp:
        json.dump(tokens, fp)

# 함수 : 토큰 파일 읽어오기
def load_tokens(filename):
    with open(filename) as fp:
        tokens = json.load(fp)
    return tokens

# 함수 : refresh_token으로 access_token 갱신
def update_tokens(app_key, filename):
    tokens = load_tokens(filename)

    url = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type": "refresh_token",
        "client_id": "key",
        "refresh_token": "Pfl43OJeOHAFUdde7yU1CFPClIlp0oU79ghmMQo9cpcAAAF8QUsHLA"
    }
    response = requests.post(url, data=data)

    # 요청 프로세스
    if response.status_code != 200:
        # 요청 실패
        print("error! because - ", response.json())
        tokens = None
    else:
        # 요청 성공
        print(response.json())
        tokens = response.json()

        # 기존 파일 백업
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = filename + "." + now
        os.rename(filename, backup_filename)

        # 갱신된 토큰 저장
        tokens['access_token'] = response.json()['access_token']
        save_tokens(filename, tokens)

    return tokens

# 함수 : 메시지 전송
def send_msg(filename, template):
    tokens = load_tokens(filename)

    headers = {"Authorization": "Bearer " + tokens['access_token']}

    # json -> string
    payload = {"template_object" : json.dumps(template)}

    # 카카오톡 전송
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    res = requests.post(url, data=payload, headers=headers)

    return res