from gtts import gTTS
from playsound import playsound

tts = gTTS(text='Halo temanku, Apa Kabar?', lang='id', slow=True)
tts.save("indonesiaLambat.mp3")
playsound("indonesiaLambat.mp3")