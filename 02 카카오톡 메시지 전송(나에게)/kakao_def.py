import requests
import json

# 카카오 토큰을 저장할 파일 명
KAKAO_TOKEN_FILENAME = "kakao_token.json"

# 함수 : json 토큰 파일 저장 프로세스
def save_tokens(filename, tokens):
    with open(filename, "w") as fp:
        json.dump(tokens, fp)