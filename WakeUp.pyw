import speech_recognition as sr
from main import Main

import sys
sys.path.append('../Body')



def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en")
        except Exception as e:
            print("No clue what you said, listening again...")
            return "No clue what you said, listening again..."
        query = str(query).lower()
        return query


def WakeUpDetected():
    WakeUpQuery = Listen().lower()

    if "wake up" in WakeUpQuery:
        print("waking up")
        Main()
    else:
        print("error")
        pass


WakeUpDetected()
