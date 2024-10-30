from gtts import gTTS
from playsound import playsound

tts = gTTS(text='Selamat pagi', lang='id', slow=False)
tts.save("morning.mp3")
playsound("morning.mp3")