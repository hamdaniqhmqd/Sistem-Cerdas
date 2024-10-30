import speech_recognition as sr

listener = sr.Recognizer()
with sr.Microphone() as input_source:
    print("Silakan berbicara kepada saya dalam bahasa Indonesia ...")
    voice_input = listener.listen(input_source)
    text = listener.recognize_google(voice_input, language='id-ID')
    print(text)
