import whisper

model=whisper.load_model("base")
result=model.transcribe("audio/whispertest.mp3")
with open("transcription.txt","w") as f:
  f.write(result["text"])