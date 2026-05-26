import pyttsx3


def speak(text: str):

    engine = pyttsx3.init()

    engine.setProperty("rate", 165)
    engine.setProperty("volume", 1.0)

    engine.say(text)
    engine.runAndWait()