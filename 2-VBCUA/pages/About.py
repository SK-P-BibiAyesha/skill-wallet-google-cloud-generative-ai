import streamlit as st
from utils.helper import load_css

load_css()

# ======================================================
# Header
# ======================================================

st.markdown("""
<div style="margin-bottom: 24px;">
    <div style="display:inline-flex; align-items:center; gap:8px; padding:4px 14px; border-radius:9999px; background:rgba(99,102,241,0.12); border:1px solid rgba(99,102,241,0.25); color:#818CF8; font-size:12px; font-weight:600; text-transform:uppercase; letter-spacing:0.06em; margin-bottom:10px;">
        System Architecture & Mission
    </div>
    <h1 style="font-size:32px; font-weight:800; margin-bottom:6px;">ℹ️ About SkillWallet VBCUA</h1>
    <p style="color:#94A3B8; font-size:16px; margin:0;">
        Deep dive into the neural foundations, acoustic pipeline, and evaluation algorithms powering Voice-Based Concept Understanding.
    </p>
</div>
""", unsafe_allow_html=True)

# Overview Card
st.markdown("""
<div class="hero-card" style="text-align:left; padding:36px 32px;">
    <div style="font-weight:700; font-size:20px; color:#F8FAFC; margin-bottom:12px;">
        💡 Project Motivation & Vision
    </div>
    <p style="margin:0 0 16px 0; max-width:100%; color:#CBD5E1; font-size:15px; line-height:1.7;">
        Traditional academic evaluations rely heavily on rote memorization or multiple-choice questions, which fail
        to measure how well a learner can articulate core technical principles in their own words.
        <strong>SkillWallet VBCUA</strong> bridges this gap by leveraging Artificial Intelligence to listen to spoken explanations,
        convert them to structured text, and evaluate their deep <em>semantic meaning</em> against expert knowledge bases.
    </p>
    <div style="display:flex; flex-wrap:wrap; gap:12px;">
        <span class="hero-stat-chip">🎯 <strong>Objective:</strong> Authentic Conceptual Assessment</span>
        <span class="hero-stat-chip">🚀 <strong>Outcome:</strong> Actionable Feedback & Verified PDF Reports</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ======================================================
# Core AI Pillars
# ======================================================

st.markdown("### 🧠 Core Architectural Pillars")
st.caption("How our multi-model AI pipeline evaluates student explanations")

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎙️</div>
        <div class="feature-title">Speech Intelligence</div>
        <div class="feature-description">
            Powered by <strong>Faster Whisper</strong>, an optimized transformer-based ASR model.
            Transcribes technical terminology accurately, normalizes audio streams, and calculates
            acoustic metrics including speaking rate (WPM) and pauses.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🧠</div>
        <div class="feature-title">Semantic Vectors</div>
        <div class="feature-description">
            Powered by <strong>Sentence-BERT</strong> (all-MiniLM-L6-v2). Embeds both the reference concept
            and student explanation into high-dimensional vector spaces to compute cosine similarity,
            capturing nuance beyond literal keywords.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">⚖️</div>
        <div class="feature-title">Multi-Modal Scoring</div>
        <div class="feature-description">
            Combines cosine similarity, keyword coverage ratio, and delivery heuristics into a unified
            Overall Score. Automatically categorizes understanding into 4 distinct mastery levels.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ======================================================
# Technology Stack
# ======================================================

st.markdown("### 🛠 Complete Technology Stack")
st.caption("Open-source frameworks and scientific libraries powering VBCUA")

tech_col1, tech_col2, tech_col3 = st.columns(3, gap="medium")

with tech_col1:
    st.markdown("""
    <div class="tech-card">
        <div class="tech-icon">🐍</div>
        <h3>Core Application</h3>
        <div class="tech-pills">
            <span class="tech-pill">Python 3.13</span>
            <span class="tech-pill">Streamlit 1.58</span>
            <span class="tech-pill">SQLite 3</span>
            <span class="tech-pill">Pandas Dataframes</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tech_col2:
    st.markdown("""
    <div class="tech-card">
        <div class="tech-icon">🤖</div>
        <h3>AI & Machine Learning</h3>
        <div class="tech-pills">
            <span class="tech-pill">Faster Whisper</span>
            <span class="tech-pill">Sentence-Transformers</span>
            <span class="tech-pill">PyTorch</span>
            <span class="tech-pill">Scikit-Learn</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tech_col3:
    st.markdown("""
    <div class="tech-card">
        <div class="tech-icon">📊</div>
        <h3>Audio & Visualization</h3>
        <div class="tech-pills">
            <span class="tech-pill">Librosa Audio NLP</span>
            <span class="tech-pill">Plotly Express</span>
            <span class="tech-pill">Matplotlib Waveforms</span>
            <span class="tech-pill">ReportLab PDF</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ======================================================
# Future Roadmap
# ======================================================

st.markdown("### 🚀 Future Roadmap & Enhancements")

f_col1, f_col2 = st.columns(2, gap="medium")

with f_col1:
    st.markdown("""
    <div class="future-card">
        <div class="future-icon">🎙️</div>
        <h3>Next-Phase Speech Intelligence</h3>
        <p>
            • <strong>Live In-Browser Audio Streaming:</strong> Direct microphone recording with real-time waveform animation.<br><br>
            • <strong>Multilingual Speech Recognition:</strong> Support for regional languages and accents.<br><br>
            • <strong>Acoustic Emotion & Confidence Analysis:</strong> Pitch variation and hesitation detection.
        </p>
    </div>
    """, unsafe_allow_html=True)

with f_col2:
    st.markdown("""
    <div class="future-card">
        <div class="future-icon">☁️</div>
        <h3>Platform Ecosystem</h3>
        <p>
            • <strong>Student & Instructor Portal:</strong> Role-based access control and student profiles.<br><br>
            • <strong>Automated Follow-up Socratic Tutor:</strong> Conversational AI bot that asks clarifying questions.<br><br>
            • <strong>Enterprise LMS Integration:</strong> Canvas, Moodle, and Google Classroom webhooks.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Metadata Note
st.markdown("""
<div style="background:rgba(99,102,241,0.08); border:1px solid rgba(99,102,241,0.25); border-radius:14px; padding:18px 24px; text-align:center;">
    <div style="font-weight:700; color:#A5B4FC; font-size:14px; margin-bottom:4px;">
        🎓 Academic Major Project • SkillWallet AI Initiative
    </div>
    <div style="color:#94A3B8; font-size:13px;">
        Developed with Google Cloud Generative AI, Open-Source Neural Networks, and Streamlit.
    </div>
</div>
""", unsafe_allow_html=True)