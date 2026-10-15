import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils.audio_validation import validate_audio_upload


def test_audio_validation():
    valid_headers = {
        "sample.wav": b"RIFF\x00\x00\x00\x00WAVE" + b"\x00" * 4,
        "sample.mp3": b"ID3" + b"\x00" * 8,
        "sample.m4a": b"\x00\x00\x00\x18ftypM4A " + b"\x00" * 4,
        "sample.ogg": b"OggS" + b"\x00" * 8,
        "sample.webm": b"\x1a\x45\xdf\xa3" + b"\x00" * 8,
    }

    for filename, content in valid_headers.items():
        assert validate_audio_upload(filename, content) is None

    assert "Unsupported file type" in validate_audio_upload("sample.txt", b"text")
    assert "empty" in validate_audio_upload("sample.ogg", b"")
    assert "larger" in validate_audio_upload("sample.ogg", b"OggSxx", max_size_bytes=4)
    assert "do not match" in validate_audio_upload("sample.ogg", b"not audio")


if __name__ == "__main__":
    test_audio_validation()
