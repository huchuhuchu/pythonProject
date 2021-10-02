import kakao_def

# 텍스트 입력받아 전송
input_text = input("나에게 보낼 메시지 : ")

# REST API KEY
KAKAO_APP_KEY = "key"

# 토큰 업데이트
tokens = kakao_def.update_tokens(KAKAO_APP_KEY,kakao_def.KAKAO_TOKEN_FILENAME)

# 업데이트 토큰 저장
kakao_def.save_tokens(kakao_def.KAKAO_TOKEN_FILENAME, tokens)

# 텍스트 템플릿 형식
template = {
    "object_type" : "text",
    "text" : input_text,
    "link" : {"web_url" : "www.naver.com"},
}

# 카카오톡 메시지 보내기
res = kakao_def.send_msg(kakao_def.KAKAO_TOKEN_FILENAME, template)

# 요청 프로세스
if res.status_code != 200:
    # 요청 실패
    print("error! because ", res.response.json())
else:
    # 요청 성공
    print("메시지 전송 성공")