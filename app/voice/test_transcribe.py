from record_audio import record_audio
from transcribe_audio import transcribe_audio


audio_file = record_audio(
    filename="test_voice.wav",
    duration=6
)

text = transcribe_audio(audio_file)

print("\nTRANSCRIPTION:\n")
print(text)