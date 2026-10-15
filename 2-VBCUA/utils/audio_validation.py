from pathlib import Path


MAX_AUDIO_UPLOAD_BYTES = 200 * 1024 * 1024


def validate_audio_upload(
    filename: str,
    content: bytes,
    max_size_bytes: int = MAX_AUDIO_UPLOAD_BYTES,
) -> str | None:
    """Return a user-facing validation error, or None for a supported audio file."""
    extension = Path(filename).suffix.lower()
    if extension not in {".wav", ".mp3", ".m4a", ".ogg", ".webm"}:
        return "Unsupported file type. Upload a WAV, MP3, M4A, OGG, or WEBM file."

    if not content:
        return "The uploaded audio file is empty."

    if len(content) > max_size_bytes:
        return f"The file is larger than the {max_size_bytes // (1024 * 1024)} MB limit."

    signatures = {
        ".wav": (
            len(content) >= 12
            and content[:4] in {b"RIFF", b"RIFX"}
            and content[8:12] == b"WAVE"
        ),
        ".mp3": (
            content.startswith(b"ID3")
            or (
                len(content) >= 2
                and content[0] == 0xFF
                and content[1] & 0xE0 == 0xE0
            )
        ),
        ".m4a": len(content) >= 8 and content[4:8] == b"ftyp",
        ".ogg": content.startswith(b"OggS"),
        ".webm": content.startswith(b"\x1a\x45\xdf\xa3"),
    }
    if not signatures[extension]:
        return (
            "The file contents do not match its audio extension. "
            "Choose a valid audio file and try again."
        )

    return None
