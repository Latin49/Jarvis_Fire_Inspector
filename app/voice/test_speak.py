import pyttsx3


engine = pyttsx3.init()

engine.setProperty("rate", 165)
engine.setProperty("volume", 1.0)

engine.say(
    "Hello Michael. Jarvis Fire Inspector voice system is now online."
)

engine.runAndWait()