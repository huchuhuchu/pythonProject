import kakao_def

# 토큰 만료 시 갱신 후 파일 저장 - 기존 토큰 파일은 시간날짜 덧붙여서 백업 파일로 저장

# 토큰 업데이트 -> 토큰 저장 필수
KAKAO_APP_KEY = "key"

tokens = kakao_def.update_tokens(KAKAO_APP_KEY, kakao_def.KAKAO_TOKEN_FILENAME)
kakao_def.save_tokens(kakao_def.KAKAO_TOKEN_FILENAME, tokens)