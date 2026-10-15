import os
import tempfile
import traceback

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
from utils.helper import load_css

load_css()

# ======================================================
# Header Section
# ======================================================

st.markdown("""
<div style="margin-bottom: 24px;">
    <div style="display:inline-flex; align-items:center; gap:8px; padding:4px 14px; border-radius:9999px; background:rgba(99,102,241,0.12); border:1px solid rgba(99,102,241,0.25); color:#818CF8; font-size:12px; font-weight:600; text-transform:uppercase; letter-spacing:0.06em; margin-bottom:10px;">
        AI Assessment Studio
    </div>
    <h1 style="font-size:32px; font-weight:800; margin-bottom:6px;">🎙️ Analyze Voice Explanation</h1>
    <p style="color:#94A3B8; font-size:16px; margin:0;">
        Upload your spoken explanation to evaluate semantic depth, keyword coverage, and speech acoustics.
    </p>
</div>
""", unsafe_allow_html=True)

# ======================================================
# Setup Grid
# ======================================================

col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.markdown("#### 1️⃣ Select Target Topic")
    topic = st.selectbox(
        "Choose the concept topic to be assessed against:",
        [
            "Machine Learning",
            "Cloud Computing",
            "Artificial Intelligence",
            "Data Science",
            "Database Management System",
            "Operating System",
        ],
        label_visibility="collapsed"
    )

    # Reference Concept Preview Expander
    with st.expander("👀 View Expert Reference Benchmark"):
        ref_preview = load_reference(topic)
        st.markdown(f"""
        <div style="background:rgba(17,24,39,0.7); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:14px; font-size:13px; color:#CBD5E1; line-height:1.6;">
            {ref_preview}
        </div>
        """, unsafe_allow_html=True)

with col_right:
    st.markdown("#### 2️⃣ Upload Voice Recording")
    uploaded_file = st.file_uploader(
        "Upload audio file (WAV, MP3, M4A, OGG, WEBM)",
        type=["wav", "mp3", "m4a", "ogg", "webm"],
        label_visibility="collapsed"
    )
    st.caption("💡 Tip: Speak clearly for 30–120 seconds in a quiet environment.")

st.markdown("<hr>", unsafe_allow_html=True)

# ======================================================
# Main Analysis Flow
# ======================================================

if uploaded_file is not None:
    # Audio Player Card
    st.markdown("""
    <div style="background:#111726; border:1px solid rgba(255,255,255,0.08); border-radius:16px; padding:20px; margin-bottom:20px;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
            <div style="font-weight:600; font-size:15px; color:#F8FAFC;">
                🎵 Ready for Assessment: <span style="color:#818CF8;">""" + uploaded_file.name + """</span>
            </div>
            <div style="font-size:12px; color:#34D399; background:rgba(16,185,129,0.12); padding:4px 10px; border-radius:8px; border:1px solid rgba(16,185,129,0.25);">
                Topic: """ + topic + """
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.audio(uploaded_file)
    st.markdown("</div>", unsafe_allow_html=True)

    # Launch Analysis Button
    if st.button("🚀 Run AI Concept Analysis", use_container_width=True, type="primary"):
        temp_audio_path = None

        try:
            with st.spinner("🧠 Transcribing audio and running S-BERT semantic embeddings..."):
                extension = os.path.splitext(uploaded_file.name)[1]

                with tempfile.NamedTemporaryFile(delete=False, suffix=extension) as temp_audio:
                    temp_audio.write(uploaded_file.read())
                    temp_audio_path = temp_audio.name

                # =====================================
                # 1. Waveform Generation
                # =====================================
                os.makedirs("audio/waveforms", exist_ok=True)
                waveform_file = f"audio/waveforms/{uploaded_file.name}.png"
                generate_waveform(temp_audio_path, waveform_file)

                # =====================================
                # 2. Speech-to-Text Transcription
                # =====================================
                transcript = transcribe_audio(temp_audio_path)

                if transcript.strip() == "":
                    st.warning("⚠️ No discernible speech detected in the audio file. Please try speaking louder and clearer.")
                    st.stop()

                # =====================================
                # 3. Audio & Acoustic Statistics
                # =====================================
                stats = analyze_audio(temp_audio_path, transcript)

                # =====================================
                # 4. Semantic Similarity & Keywords
                # =====================================
                reference = load_reference(topic)
                similarity = calculate_similarity(reference, transcript)
                keyword_result = match_keywords(reference, transcript)
                score = generate_score(similarity)
                feedback = generate_feedback(similarity)

                # =====================================
                # 5. Database Save & PDF Generation
                # =====================================
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

                os.makedirs("reports", exist_ok=True)
                pdf_file = f"reports/{topic}_Analysis_Report.pdf"
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

            # ==================================================
            # RENDER BEAUTIFUL RESULTS DASHBOARD
            # ==================================================
            st.success("✅ Analysis Complete! Your speech has been evaluated successfully.")

            # Top Score Banner
            st.markdown("### 🎯 Overall Understanding Evaluation")

            level_cls = "level-banner-high" if similarity >= 80 else ("level-banner-mid" if similarity >= 65 else "level-banner-low")
            level_icon = "🟢" if similarity >= 80 else ("🟡" if similarity >= 65 else "🔴")

            st.markdown(f"""
            <div class="level-banner {level_cls}">
                <div style="font-size:32px;">{level_icon}</div>
                <div>
                    <div style="font-size:13px; font-weight:700; text-transform:uppercase; letter-spacing:0.05em;">Assessed Performance Level</div>
                    <div style="font-size:22px; font-weight:800; font-family:var(--font-heading);">{feedback['level']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # 3 KPI Cards
            score_col1, score_col2, score_col3 = st.columns(3)

            with score_col1:
                st.markdown(f"""
                <div class="score-kpi-card">
                    <div class="score-kpi-label">Overall Mastery Score</div>
                    <div class="score-kpi-val" style="color:#818CF8;">{score['overall']:.1f}%</div>
                </div>
                """, unsafe_allow_html=True)

            with score_col2:
                st.markdown(f"""
                <div class="score-kpi-card">
                    <div class="score-kpi-label">Concept Accuracy</div>
                    <div class="score-kpi-val" style="color:#34D399;">{score['concept']:.1f}%</div>
                </div>
                """, unsafe_allow_html=True)

            with score_col3:
                st.markdown(f"""
                <div class="score-kpi-card">
                    <div class="score-kpi-label">Explanation Quality</div>
                    <div class="score-kpi-val" style="color:#38BDF8;">{score['quality']:.1f}%</div>
                </div>
                """, unsafe_allow_html=True)

            # Progress Bars
            st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)
            prog_col1, prog_col2, prog_col3 = st.columns(3)

            with prog_col1:
                st.caption(f"Overall Score: {score['overall']:.1f}%")
                st.progress(score["overall"] / 100)

            with prog_col2:
                st.caption(f"Concept Accuracy: {score['concept']:.1f}%")
                st.progress(score["concept"] / 100)

            with prog_col3:
                st.caption(f"Explanation Quality: {score['quality']:.1f}%")
                st.progress(score["quality"] / 100)

            st.markdown("<hr>", unsafe_allow_html=True)

            # =====================================
            # Concept Comparison
            # =====================================
            st.markdown("### 📖 Concept Comparison Breakdown")
            st.caption("Side-by-side comparison of your explanation against the expert standard benchmark")

            comp_left, comp_right = st.columns(2, gap="medium")

            with comp_left:
                st.markdown(f"""
                <div class="comparison-box" style="border-top:3px solid #6366F1;">
                    <div class="comparison-header">
                        <span style="font-size:20px;">📘</span>
                        <span style="color:#A5B4FC;">Expert Reference Knowledge</span>
                    </div>
                    <div class="comparison-content">
                        {reference}
                    </div>
                </div>
                """, unsafe_allow_html=True)

            with comp_right:
                st.markdown(f"""
                <div class="comparison-box" style="border-top:3px solid #10B981;">
                    <div class="comparison-header">
                        <span style="font-size:20px;">🎙️</span>
                        <span style="color:#34D399;">Transcribed Student Explanation</span>
                    </div>
                    <div class="comparison-content">
                        {transcript}
                    </div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("<hr>", unsafe_allow_html=True)

            # =====================================
            # Keyword Analysis
            # =====================================
            st.markdown("### 🔑 Technical Keyword Analysis")
            st.caption(f"Matched {keyword_result['matched_count']} of {keyword_result['total']} domain terms ({keyword_result['score']}% keyword coverage)")

            kw_col1, kw_col2 = st.columns(2, gap="medium")

            with kw_col1:
                st.markdown("##### ✅ Matched Technical Terms")
                if keyword_result["matched"]:
                    pills_html = "".join([f'<span class="keyword-badge keyword-badge-matched">✓ {kw}</span>' for kw in keyword_result["matched"]])
                    st.markdown(f'<div class="keyword-container-box">{pills_html}</div>', unsafe_allow_html=True)
                else:
                    st.markdown('<div class="keyword-container-box"><span style="color:#94A3B8; font-size:13.5px;">No primary reference keywords detected.</span></div>', unsafe_allow_html=True)

            with kw_col2:
                st.markdown("##### ⚠️ Missing Technical Terms")
                if keyword_result["missing"]:
                    pills_html = "".join([f'<span class="keyword-badge keyword-badge-missing">✕ {kw}</span>' for kw in keyword_result["missing"]])
                    st.markdown(f'<div class="keyword-container-box">{pills_html}</div>', unsafe_allow_html=True)
                else:
                    st.markdown('<div class="keyword-container-box"><span style="color:#34D399; font-weight:600; font-size:13.5px;">Outstanding! All reference terms covered 🎉</span></div>', unsafe_allow_html=True)

            st.markdown("<hr>", unsafe_allow_html=True)

            # =====================================
            # Acoustic & Audio Statistics
            # =====================================
            st.markdown("### 🎵 Speech Acoustics & Pacing")
            st.caption("Biometric and delivery statistics extracted from your recorded audio")

            m1, m2, m3, m4, m5 = st.columns(5)

            with m1:
                st.metric("⏱ Duration", f"{stats['duration']} s")

            with m2:
                st.metric("📝 Word Count", f"{stats['word_count']} words")

            with m3:
                speech_rate = stats['speech_rate']
                pacing_badge = "Ideal" if 120 <= speech_rate <= 160 else ("Fast" if speech_rate > 160 else "Slow")
                st.metric("🗣 Speech Rate", f"{speech_rate} WPM", delta=pacing_badge, delta_color="normal")

            with m4:
                st.metric("🔊 Audio Energy", f"{stats['energy']:.3f}")

            with m5:
                st.metric("🤫 Silence Ratio", f"{stats['silence']}%")

            # Waveform Display
            if os.path.exists(waveform_file):
                st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)
                st.image(waveform_file, use_container_width=True)

            st.markdown("<hr>", unsafe_allow_html=True)

            # =====================================
            # AI Feedback & Recommendations
            # =====================================
            st.markdown("### 💬 AI Qualitative Feedback & Guidance")

            st.markdown(f"""
            <div style="background:#111726; border:1px solid rgba(99,102,241,0.25); border-radius:18px; padding:24px; margin-bottom:24px; box-shadow:0 8px 30px -10px rgba(0,0,0,0.5);">
                <div style="font-weight:700; font-size:16px; color:#A5B4FC; margin-bottom:8px; display:flex; align-items:center; gap:8px;">
                    <span>🤖</span> AI Concept Advisor Feedback
                </div>
                <div style="font-size:15px; color:#E2E8F0; line-height:1.7;">
                    {feedback['message']}
                </div>
            </div>
            """, unsafe_allow_html=True)

            # =====================================
            # PDF Download Button
            # =====================================
            st.markdown("### 📄 Export Official Assessment Report")

            with open(pdf_file, "rb") as pdf:
                st.download_button(
                    label="📥 Download Official Assessment Report (PDF)",
                    data=pdf,
                    file_name=f"{topic}_Analysis_Report.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                    type="primary"
                )

        except Exception as e:
            st.error(f"❌ An error occurred during analysis: {e}")
            st.code(traceback.format_exc())

        finally:
            if temp_audio_path is not None and os.path.exists(temp_audio_path):
                os.remove(temp_audio_path)

else:
    st.info("📂 Please upload an audio recording above to launch the AI analysis.")
