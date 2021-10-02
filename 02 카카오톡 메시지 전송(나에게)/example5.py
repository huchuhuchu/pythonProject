import kakao_def

# 함수 파일 분리 및 import를 통한 코드 간소화

KAKAO_APP_KEY = "key"

# 토큰 업데이트
tokens = kakao_def.update_tokens(KAKAO_APP_KEY,kakao_def.KAKAO_TOKEN_FILENAME)

# 업데이트 토큰 저장
kakao_def.save_tokens(kakao_def.KAKAO_TOKEN_FILENAME, tokens)

# 텍스트 템플릿 형식
template = {
    "object_type" : "text",
    "text" : "Hello, world!!!@@",
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