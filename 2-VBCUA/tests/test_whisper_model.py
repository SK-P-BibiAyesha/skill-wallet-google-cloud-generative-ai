import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from models.whisper_model import transcribe_audio


def test_whisper_model():
    """
    Test Faster Whisper transcription.
    """

    audio_path = "tests/sample_audio.ogg"

    transcript = transcribe_audio(audio_path)

    print("\nTranscript:")
    print(transcript)

    # Verify return type
    assert isinstance(transcript, str)

    # Transcript should not be empty
    assert len(transcript) > 0

    # Basic sanity check
    assert len(transcript.split()) >= 3

    print("\n✅ Whisper Model Test Passed")


if __name__ == "__main__":
    test_whisper_model()