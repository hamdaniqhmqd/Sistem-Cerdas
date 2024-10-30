import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty('rate', 120)
engine.setProperty('volume', 1)

def listen():
    listener = sr.Recognizer()
    with sr.Microphone() as input_source:
        print("Silakan berbicara...")
        voice_input = listener.listen(input_source)
        text = listener.recognize_google(voice_input, language='id-ID')
        print(f"Anda mengatakan: {text}")
    
    if text:
      return text
    else:
      thanks()

def hobi():
    hobi_input = listen()
    if hobi_input:
        print(f"Wow, hobi anda adalah {hobi_input}")
        engine.say(f"Wow, hobi anda adalah {hobi_input}")
        engine.runAndWait()
    else:
        thanks()

def thanks():
    print("Terima Kasih")
    engine.say("Terima Kasih")
    engine.runAndWait()

def nama():
    print("siapa nama anda:")
    engine.say("siapa nama anda:")
    engine.runAndWait()
    nama = listen()

    if nama:
        print(f"Baik {nama}, apa hobi anda")
        engine.say(f"Baik {nama}, apa hobi anda")
        engine.runAndWait()
        hobi()
    else:
        thanks()

nama()