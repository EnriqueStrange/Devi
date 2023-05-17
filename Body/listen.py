import googletrans
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
            query = r.recognize_google(audio, language='hi')
            print(f"user said: {query}\n")
        except Exception as e:
            print("No clue what you said, listening again...")
            return "None"
        return query
        


