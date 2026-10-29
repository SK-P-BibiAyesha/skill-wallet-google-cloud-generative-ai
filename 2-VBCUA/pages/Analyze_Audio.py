import os
import hashlib
import logging
import tempfile

import streamlit as st

from models.whisper_model import transcribe_audio
from models.semantic_model import calculate_similarity
from models.audio_analysis import analyze_audio
from models.keyword_match import match_keywords
from models.scoring import generate_score
from models.feedback import generate_feedback

from utils.reference_loader import load_reference
from utils.visualization import generate_waveform
from utils.pdf_generator import generate_pdf

from database.queries import insert_analysis
from utils.audio_validation import validate_audio_upload


from utils.helper import load_css

load_css()

logger = logging.getLogger(__name__)

st.title("🎤 Analyze Audio")
st.caption("Upload a voice explanation to compare it with the selected reference concept.")

st.divider()


# ======================================================
# Topic Selection
# ======================================================

topic = st.selectbox(
    "📚 Select Topic",
    [
        "Machine Learning",
        "Cloud Computing",
        "Artificial Intelligence",
        "Data Science",
        "Database Management System",
        "Operating System",
    ]
)

st.divider()


# ======================================================
# Upload Audio
# ======================================================

uploaded_file = st.file_uploader(
    "🎵 Upload Audio File",
    type=["wav", "mp3", "m4a", "ogg", "webm"]
)


# ======================================================
# Main Analysis
# ======================================================

if uploaded_file is not None:

    audio_bytes = uploaded_file.getvalue()
    validation_error = validate_audio_upload(uploaded_file.name, audio_bytes)
    if validation_error:
        st.error(validation_error)
        st.stop()

    st.success(f"Uploaded: {uploaded_file.name}")
    st.caption(f"File size: {len(audio_bytes) / (1024 * 1024):.2f} MB")

    audio_format = uploaded_file.type or "audio/ogg"

    st.write("**Upload diagnostics**")
    st.write("Filename:", uploaded_file.name)
    st.write("File type:", audio_format)
    st.write("Bytes received:", len(audio_bytes))

    st.audio(audio_bytes, format=audio_format)

    st.info(f"Selected Topic: **{topic}**")

    upload_fingerprint = hashlib.sha256(
        topic.encode("utf-8") + b"\0" + audio_bytes
    ).hexdigest()
    previously_analyzed = (
        st.session_state.get("last_analysis_fingerprint") == upload_fingerprint
    )

    if previously_analyzed:
        st.info(
            "This audio and topic have already been analyzed in this session. "
            "View the saved result in Reports, or explicitly analyze it again."
        )
        if st.button(
            "Analyze This Audio Again",
            width="stretch",
            key="reanalyze-same-upload",
        ):
            st.session_state.pop("last_analysis_fingerprint", None)
            st.rerun()
    elif st.button("🚀 Analyze Audio", width="stretch"):

        temp_audio_path = None

        try:

            with st.spinner("Analyzing audio..."):

                extension = os.path.splitext(
                    uploaded_file.name
                )[1]

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=extension
                ) as temp_audio:

                    temp_audio.write(audio_bytes)

                    temp_audio_path = temp_audio.name

                # =====================================
                              # =====================================
                # Speech To Text (run first)
                # =====================================

                st.info("Step 1/4: Transcribing speech...")
                transcript = transcribe_audio(temp_audio_path)

                if not transcript.strip():
                    st.warning("⚠ No speech detected in this audio file.")
                    st.stop()

                st.success("✅ Transcription completed")

                # =====================================
                # Waveform (optional visualization)
                # =====================================

                st.info("Step 2/4: Preparing waveform...")

                try:
                    os.makedirs("audio/waveforms", exist_ok=True)
                    waveform_file = (
                        f"audio/waveforms/{upload_fingerprint}.png"
                    )

                    generate_waveform(temp_audio_path, waveform_file)

                    if (
                        os.path.exists(waveform_file)
                        and os.path.getsize(waveform_file) > 0
                    ):
                        st.subheader("📈 Audio Waveform")
                        st.image(waveform_file, width="stretch")
                    else:
                        st.warning(
                            "Waveform could not be generated; "
                            "continuing with analysis."
                        )

                except Exception:
                    logger.exception("Waveform generation failed.")
                    st.warning(
                        "Waveform visualization failed, "
                        "but speech analysis will continue."
                    )

                # =====================================
                # Audio Statistics
                # =====================================

                stats = analyze_audio(
                    temp_audio_path,
                    transcript
                )

                st.subheader(
                    "🎵 Audio Statistics"
                )

                col1, col2, col3, col4, col5 = st.columns(5)

                with col1:
                    st.metric(
                        "⏱ Duration",
                        f"{stats['duration']} sec"
                    )

                with col2:
                    st.metric(
                        "📝 Words",
                        stats["word_count"]
                    )

                with col3:
                    st.metric(
                        "🗣 Speech Rate",
                        f"{stats['speech_rate']} WPM"
                    )

                with col4:
                    st.metric(
                        "🔊 Loudness",
                        stats["energy"]
                    )

                with col5:
                    st.metric(
                        "🤫 Silence",
                        f"{stats['silence']}%"
                    )


                # =====================================
                # Reference Concept
                # =====================================

                reference = load_reference(topic)

                # =====================================
                # Semantic Similarity
                # =====================================

                similarity = calculate_similarity(
                    reference,
                    transcript
                )

                # =====================================
                # Keyword Matching
                # =====================================

                keyword_result = match_keywords(
                    reference,
                    transcript
                )

                # =====================================
                # Concept Comparison
                # =====================================

                st.subheader("📖 Concept Comparison")

                left, right = st.columns(2)

                with left:

                    st.markdown("### 📘 Reference Concept")

                    st.info(reference)

                with right:

                    st.markdown("### 🎤 Student Explanation")

                    st.success(transcript)

                # =====================================
                # Similarity Badge
                # =====================================

                if similarity >= 85:

                    st.success("🟢 High Concept Match")

                elif similarity >= 70:

                    st.info("🟡 Moderate Concept Match")

                else:

                    st.warning("🔴 Low Concept Match")

                # =====================================
                # Keyword Matching Results
                # =====================================

                st.divider()

                st.subheader("🔑 Keyword Matching")

                col1, col2 = st.columns(2)

                with col1:

                    st.markdown("### ✅ Matched Keywords")

                    if keyword_result["matched"]:

                        st.write(
                            ", ".join(
                                keyword_result["matched"]
                            )
                        )

                    else:

                        st.info(
                            "No matched keywords."
                        )

                with col2:

                    st.markdown("### ❌ Missing Keywords")

                    if keyword_result["missing"]:

                        st.write(
                            ", ".join(
                                keyword_result["missing"]
                            )
                        )

                    else:

                        st.success("None 🎉")

                st.metric(
                    "Keyword Match Score",
                    f"{keyword_result['score']}%"
                )

                st.caption(
                    f"Matched {keyword_result['matched_count']} "
                    f"of {keyword_result['total']} "
                    f"reference keywords."
                )

                # =====================================
                # Score Generation
                # =====================================

                score = generate_score(
                    similarity
                )

                st.divider()

                st.subheader("📊 Analysis Scores")

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(
                        "Overall Score",
                        f"{score['overall']:.2f}%"
                    )

                with col2:

                    st.metric(
                        "Concept Accuracy",
                        f"{score['concept']:.2f}%"
                    )

                with col3:

                    st.metric(
                        "Explanation Quality",
                        f"{score['quality']:.2f}%"
                    )

                # =====================================
                # Performance Bars
                # =====================================

                st.subheader("📈 Performance")

                st.write("Overall Score")

                st.progress(
                    score["overall"] / 100
                )

                st.write("Concept Accuracy")

                st.progress(
                    score["concept"] / 100
                )

                st.write("Explanation Quality")

                st.progress(
                    score["quality"] / 100
                )

                # =====================================
                # AI Verdict
                # =====================================

                st.divider()

                st.subheader("📌 Result Summary")

                if similarity >= 90:

                    st.success(
                        "The student's explanation demonstrates an excellent understanding of the selected concept."
                    )

                elif similarity >= 75:

                    st.info(
                        "The student understands most of the concept but can improve by including more technical details."
                    )

                else:

                    st.warning(
                        "The explanation covers only part of the concept. More practice is recommended."
                    )


                # =====================================
                # Feedback
                # =====================================

                feedback = generate_feedback(
                    similarity
                )

                st.divider()

                st.subheader("🎯 Understanding Level")

                if feedback["color"] == "success":

                    st.success(feedback["level"])

                elif feedback["color"] == "info":

                    st.info(feedback["level"])

                elif feedback["color"] == "warning":

                    st.warning(feedback["level"])

                else:

                    st.error(feedback["level"])

                st.subheader("💬 Feedback")

                st.write(
                    feedback["message"]
                )

                # =====================================
                # Generate PDF
                # =====================================

                os.makedirs(
                    "reports",
                    exist_ok=True
                )

                pdf_file = (
                    f"reports/{topic}_Analysis_Report.pdf"
                )

                generate_pdf(
                    filename=pdf_file,
                    topic=topic,
                    transcript=transcript,
                    similarity=similarity,
                    overall=score["overall"],
                    concept=score["concept"],
                    quality=score["quality"],
                    level=feedback["level"],
                    feedback=feedback["message"],
                )

                # Save only after the report has been generated successfully.
                insert_analysis(
                    topic=topic,
                    transcript=transcript,
                    similarity=similarity,
                    overall=score["overall"],
                    concept=score["concept"],
                    quality=score["quality"],
                    level=feedback["level"],
                    feedback=feedback["message"],
                )
                st.session_state["last_analysis_fingerprint"] = upload_fingerprint

                # =====================================
                # Download PDF
                # =====================================

                st.divider()

                st.subheader("📄 Download Report")

                with open(
                    pdf_file,
                    "rb"
                ) as pdf:

                    st.download_button(
                        label="📥 Download PDF Report",
                        data=pdf,
                        file_name=f"{topic}_Analysis_Report.pdf",
                        mime="application/pdf",
                        width="stretch",
                    )

                st.success(
                    "✅ Analysis Completed Successfully!"
                )

        except Exception as error:
            logger.exception("Audio analysis failed.")
            st.error(f"Audio analysis failed: {error}")

        finally:

            if (
                temp_audio_path is not None
                and os.path.exists(temp_audio_path)
            ):

                os.remove(
                    temp_audio_path
                )

else:

    st.info(
        "📂 Please upload an audio file to begin analysis."
    )
                    
