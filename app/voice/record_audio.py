import sounddevice as sd
from scipy.io.wavfile import write


def record_audio(filename="voice_input.wav", duration=6, sample_rate=44100):
    print("Recording... speak now.")

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1
    )

    sd.wait()

    write(filename, sample_rate, audio)

    print(f"Recording saved to {filename}")

    return filename