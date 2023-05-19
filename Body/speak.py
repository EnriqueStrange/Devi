import pyttsx3


def Speak(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.setProperty("rate", 180)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    print("")
    print(f"You : {text}")
    print("")
    engine.say(text)
    engine.runAndWait()
