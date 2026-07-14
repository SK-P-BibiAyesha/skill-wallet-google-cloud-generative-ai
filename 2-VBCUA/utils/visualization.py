import librosa
import librosa.display
import matplotlib.pyplot as plt
import os


def generate_waveform(audio_path, output_path):
    """
    Generate a waveform image from an audio file.
    """

    # Load audio
    y, sr = librosa.load(audio_path, sr=None)

    # Create figure
    plt.figure(figsize=(10, 3))

    librosa.display.waveshow(
        y,
        sr=sr
    )

    plt.title("Audio Waveform")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")

    plt.tight_layout()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    plt.savefig(output_path)

    plt.close()