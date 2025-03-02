import base64

base64_audio = "인코딩 데이터"
audio_data = base64.b64decode(base64_audio)

with open("output.wav", "wb") as f:
    f.write(audio_data)

print("오디오 파일 저장 완료: output.wav")