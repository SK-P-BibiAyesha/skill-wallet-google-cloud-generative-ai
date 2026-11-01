import os
import librosa
import librosa.display
import matplotlib.pyplot as plt


def generate_waveform(audio_path, output_path):
    """
    Generate and save a waveform image from an audio file.
    """

    y, sr = librosa.load(audio_path, sr=None)

    output_dir = os.path.dirname(output_path)

    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    fig, ax = plt.subplots(figsize=(12, 3))

    librosa.display.waveshow(y, sr=sr, ax=ax)

    ax.set_title("Audio Waveform")
    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("Amplitude")

    fig.tight_layout()

    fig.savefig(
        output_path,
        format="png",
        dpi=150,
        bbox_inches="tight"
    )

    plt.close(fig)

    return output_path