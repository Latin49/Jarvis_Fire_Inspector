import sys

sys.path.append("app")
sys.path.append("app/knowledge")
sys.path.append("app/web_research")
sys.path.append("app/voice")


from record_audio import record_audio
from transcribe_audio import transcribe_audio
from hybrid_answer import answer_with_hybrid_research
from openai_tts import speak_natural


EXIT_WORDS = [
    "exit",
    "quit",
    "stop",
    "shutdown",
    "shut down",
    "goodbye jarvis",
    "that's all jarvis"
]


def should_exit(text: str) -> bool:
    text = text.lower()

    for word in EXIT_WORDS:
        if word in text:
            return True

    return False


def run_jarvis():

    print("\nJarvis Fire Inspector Online")
    print("Say a fire inspection question.")
    print("Say 'shutdown' or 'goodbye Jarvis' to stop.\n")

    speak_natural(
        "Jarvis Fire Inspector online. How can I assist with your inspection?"
    )

    while True:

        audio_file = record_audio(
            filename="jarvis_input.wav",
            duration=8
        )

        print("\nTranscribing...\n")

        user_text = transcribe_audio(audio_file)

        print(f"\nYOU SAID:\n{user_text}\n")

        if should_exit(user_text):
            print("Jarvis shutting down.")
            speak_natural("Understood. Jarvis shutting down.")
            break

        print("Jarvis is thinking...\n")

        answer = answer_with_hybrid_research(user_text)

        print(f"\nJARVIS:\n{answer}\n")

        speak_natural(answer)


if __name__ == "__main__":
    run_jarvis()