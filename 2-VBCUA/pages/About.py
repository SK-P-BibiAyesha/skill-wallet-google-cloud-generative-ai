import streamlit as st
from utils.helper import load_css

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

load_css()

st.title("ℹ️ About VBCUA")

st.markdown("""
# 🎤 Voice-Based Concept Understanding Analyser

The **Voice-Based Concept Understanding Analyser (VBCUA)** is an AI-powered web application that evaluates a student's conceptual understanding through spoken explanations.

Instead of checking for exact words, the system measures the **semantic meaning** of the student's explanation using Artificial Intelligence.
""")

st.divider()

# ---------------------------------
# Features
# ---------------------------------

st.header("✨ Features")

col1, col2 = st.columns(2)

with col1:
    st.success("🎤 Audio Upload")
    st.success("📝 Speech-to-Text")
    st.success("🧠 Semantic Similarity")
    st.success("📊 AI Score Generation")

with col2:
    st.success("💬 AI Feedback")
    st.success("📄 PDF Report")
    st.success("📈 Dashboard Analytics")
    st.success("💾 SQLite Database")

st.divider()

# ---------------------------------
# Technologies
# ---------------------------------

st.header("🛠 Technologies Used")

st.markdown("""
- **Python**
- **Streamlit**
- **Faster Whisper**
- **Sentence-BERT**
- **SQLite**
- **ReportLab**
- **Librosa**
- **Matplotlib**
- **Plotly**
""")

st.divider()

# ---------------------------------
# Workflow
# ---------------------------------

st.header("⚙️ System Workflow")

st.markdown("""
1. Upload Audio

2. Speech Transcription (Whisper)

3. Load Reference Concept

4. Semantic Similarity (Sentence-BERT)

5. Score Calculation

6. AI Feedback Generation

7. Store Result in Database

8. Generate PDF Report

9. Display Dashboard Analytics
""")

st.divider()

# ---------------------------------
# Future Scope
# ---------------------------------

st.header("🚀 Future Scope")

st.markdown("""
- Live voice recording
- Multi-language support
- AI chatbot tutor
- Cloud deployment
- Student login system
- Teacher dashboard
- Performance prediction
""")

st.divider()

st.info("Developed as an AI-based educational project using Machine Learning and Natural Language Processing.")