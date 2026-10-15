import os
import librosa
import librosa.display
import matplotlib.pyplot as plt


def generate_waveform(audio_path, output_path):
    """
    Generate a modern dark-themed waveform image from an audio file.
    """
    # Load audio
    y, sr = librosa.load(audio_path, sr=None)

    # Create styled figure matching the dark theme
    fig, ax = plt.subplots(figsize=(10, 2.8), facecolor="#111827")
    ax.set_facecolor("#111827")

    # Plot wave with vibrant indigo color and subtle alpha
    librosa.display.waveshow(
        y,
        sr=sr,
        ax=ax,
        color="#818CF8",
        alpha=0.85
    )

    # Styling title & labels
    ax.set_title("Speech Acoustic Waveform", color="#F8FAFC", fontsize=12, fontweight="600", pad=10)
    ax.set_xlabel("Time (seconds)", color="#94A3B8", fontsize=10, labelpad=6)
    ax.set_ylabel("Amplitude", color="#94A3B8", fontsize=10, labelpad=6)

    # Ticks & spines
    ax.tick_params(colors="#94A3B8", labelsize=9)
    for spine in ax.spines.values():
        spine.set_color("#334155")
        spine.set_linewidth(1.0)

    # Subtle horizontal center guide
    ax.axhline(0, color="#475569", linestyle="--", linewidth=0.8, alpha=0.6)

    plt.tight_layout()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, facecolor=fig.get_facecolor(), edgecolor="none", dpi=160)
    plt.close(fig)