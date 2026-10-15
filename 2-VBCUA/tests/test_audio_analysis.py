import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from models.audio_analysis import analyze_audio


def test_audio_analysis():
    """
    Test audio analysis function using a sample audio file.
    """

    audio_path = Path(__file__).resolve().parent / "cloud.ogg"

    transcript = (
        "Cloud computing provides on demand access "
        "to computing resources over the internet."
    )

    result = analyze_audio(audio_path, transcript)

    print("Returned value:", result)
    print("Type:", type(result))

    assert isinstance(result, dict)

    assert "duration" in result
    assert "word_count" in result
    assert "speech_rate" in result
    assert "energy" in result
    assert "silence" in result

    assert isinstance(result["duration"], float)
    assert isinstance(result["word_count"], int)
    assert isinstance(result["speech_rate"], float)
    assert isinstance(result["energy"], float)
    assert isinstance(result["silence"], float)

    assert result["duration"] > 0
    assert result["word_count"] > 0
    assert result["speech_rate"] > 0
    assert result["energy"] >= 0
    assert 0 <= result["silence"] <= 100

    print("✅ Audio Analysis Test Passed")


if __name__ == "__main__":
    test_audio_analysis()