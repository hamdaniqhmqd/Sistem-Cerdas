import pyttsx3

engine = pyttsx3.init()
                      
engine.setProperty('rate', 70)                           
engine.setProperty('volume',0.5)   
voices = engine.getProperty('voices')      
engine.setProperty('voice', voices[1].id) 

engine.say("Selamat pagi, nama saya ahmad")
engine.runAndWait()