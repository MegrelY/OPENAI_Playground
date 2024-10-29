from openai import OpenAI
client = OpenAI()

audio_file= open("portest.mp3", "rb")
translation = client.audio.translations.create(
  model="whisper-1", 
  file=audio_file
)
print(translation.text)

with open("transcription.txt", "w" ) as text_file:
    text_file.write(translation.text)