from googletrans import Translator
import speech_recognition as sr


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
            return "No clue what you said, listening again..."
        query = str(query).lower()
        return query


def TranslattionHindiToEnglish(text):
    line = str(text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    return data


def MicConnect():
    query = Listen()
    data = TranslattionHindiToEnglish(query)
    return data
