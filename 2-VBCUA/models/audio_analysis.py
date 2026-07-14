import librosa
import numpy as np


def analyze_audio(audio_path, transcript):
    """
    Analyze audio and return basic statistics.
    """

    # Load audio
    y, sr = librosa.load(audio_path, sr=None)

    # Duration (seconds)
    duration = librosa.get_duration(y=y, sr=sr)

    # RMS Energy (average loudness)
    rms = librosa.feature.rms(y=y)
    average_energy = float(np.mean(rms))

    # -----------------------------------
    # Silence Detection
    # -----------------------------------

    intervals = librosa.effects.split(
        y,
        top_db=30
    )

    speech_samples = sum(
        end - start
        for start, end in intervals
    )

    speech_duration = speech_samples / sr

    silence_duration = duration - speech_duration

    silence_percentage = (
        silence_duration / duration
    ) * 100 if duration > 0 else 0

    # Word count
    words = len(transcript.split())

    # Words per minute
    if duration > 0:
        speech_rate = (words / duration) * 60
    else:
        speech_rate = 0

        
    print({
    "duration": round(duration, 2),
    "word_count": words,
    "speech_rate": round(speech_rate, 2),
    "energy": round(average_energy, 4),
    "silence": round(silence_percentage, 2),
})

    return {
        "duration": round(duration, 2),
        "word_count": words,
        "speech_rate": round(speech_rate, 2),
        "energy": round(average_energy, 4),
        "silence": round(silence_percentage, 2),
    }