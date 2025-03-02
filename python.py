import base64

base64_audio = "인코딩 데이터"
audio_data = base64.b64decode(base64_audio)

with open("output.wav", "wb") as f:
    f.write(audio_data)

print("오디오 파일 저장 완료: output.wav")

import os

print("현재 작업 디렉토리:", os.getcwd())  # 현재 경로 출력
print("파일 목록:", os.listdir())  # 현재 디렉토리에 있는 파일들 확인