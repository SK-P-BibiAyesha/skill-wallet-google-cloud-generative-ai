from faster_whisper import WhisperModel
import streamlit as st


@st.cache_resource
def load_whisper_model():
    model = WhisperModel(
        "base",
        device="cpu",
        compute_type="int8"
    )
    return model


def transcribe_audio(audio_path):
    try:
        model = load_whisper_model()

        segments, info = model.transcribe(
            audio_path,
            beam_size=5
        )

        transcript = ""

        for segment in segments:
            transcript += segment.text + " "

        return transcript.strip()

    except Exception as e:
        raise RuntimeError(f"Whisper Error: {e}") from e