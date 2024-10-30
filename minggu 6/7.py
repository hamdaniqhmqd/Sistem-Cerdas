import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 120)
engine.setProperty('volume', 1)

def hobi():
    hobi = input("Masukkan Hobi anda : ")
    if hobi:
        engine.say(f"Wow, hobi anda adalah {hobi}")
        print(f"Wow, hobi anda adalah {hobi}")
        engine.runAndWait()
    else:
        thanks()

def thanks():
    engine.say("Terima Kasih")
    print("Terima Kasih")
    engine.runAndWait()

engine.say("Masukkan nama anda : ")
engine.runAndWait()

nama = input("Masukkan nama anda : ")

if nama:
    engine.say(f"Baik {nama}, silahkan masukkan hobi anda")
    print(f"Baik {nama}, silahkan masukkan hobi anda")
    engine.runAndWait()
    hobi()
else:
    thanks()
