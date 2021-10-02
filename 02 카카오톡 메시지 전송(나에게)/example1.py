import requests
import json
import kakao_def

# Kakao API 토큰 발급 및 출력

# https://kauth.kakao.com/oauth/authorize?client_id=<RESTAPI 키>&response_type=code&redirect_uri=https://localhost.com
# https://localhost.com/?code=<해당 부분 사용>


url = "https://kauth.kakao.com/oauth/token"

# client_id : REST KEY
# code : code
data = {
    "grant_type" : "authorization_code",
    "client_id" : "key",
    "redirect_uri" : "https://localhost.com",
    "code" : "nZcb3zOvVxFS69wyD3aj7UwenTOZ4U3-FltMXToCWBLMbypp0v2Gtwqs1uqq_W9t1nYUZAo9dGkAAAF8QUpjYA"
}

response = requests.post(url, data=data)

# 사용자 토큰 발급 프로세스
if response.status_code != 200:
    # 요청 성공
    print("error! because ", response.json())
else:
    # 요청 성공
    tokens = response.json()
    kakao_def.save_tokens(kakao_def.KAKAO_TOKEN_FILENAME, tokens)
    print(tokens)


"""
응답 분석
access_token : 사용자 액세스 토큰 값
token_type : 토큰 파일 bearer 고정
refresh_token : 토큰 만료 시 access_token 재발급
expires_in : 토큰 유효 활성화 시간
scope : 권한 범위
refresh_token_expires_in : refresh_token의 유효 활성화 시간
"""
"""
{'access_token': 'DyKNZ7ey5HxngSCRk7muKuZUDY5BHzgnWrcHTQo9cpcAAAF8QUsHLQ', 
'token_type': 'bearer', 
'refresh_token': 'Pfl43OJeOHAFUdde7yU1CFPClIlp0oU79ghmMQo9cpcAAAF8QUsHLA', 
'expires_in': 21599, 
'scope': 'account_email talk_message profile_nickname', 
'refresh_token_expires_in': 5183999}
"""