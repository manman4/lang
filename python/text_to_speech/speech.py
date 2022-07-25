from gtts import gTTS
from playsound import playsound

tts = gTTS(text='こんにちは', lang='ja')
tts.save('hello.mp3')
playsound("hello.mp3")