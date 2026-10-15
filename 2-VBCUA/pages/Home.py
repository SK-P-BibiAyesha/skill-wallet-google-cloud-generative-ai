import streamlit as st
from utils.helper import load_css

load_css()

# ---------------------------------
# Hero Section
# ---------------------------------

st.markdown("""
<div class="hero-card">
    <div class="hero-badge">
        ✨ Next-Gen Educational AI • Voice Concept Intelligence
    </div>
    <h1>Master Technical Concepts Through Voice</h1>
    <p>
        The Voice-Based Concept Understanding Analyser (VBCUA) transforms spoken explanations
        into deep semantic insights. Evaluate conceptual understanding with state-of-the-art
        ASR transcription, NLP semantic vectors, and automated feedback.
    </p>
    <div class="hero-stats-row">
        <div class="hero-stat-chip">🎙️ <span>Faster-Whisper</span> Speech ASR</div>
        <div class="hero-stat-chip">🧠 <span>Sentence-BERT</span> Semantic Vectors</div>
        <div class="hero-stat-chip">🔑 <span>Keyword & Coverage</span> Analysis</div>
        <div class="hero-stat-chip">📄 <span>Instant PDF</span> Performance Reports</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Quick Action Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 Start Voice Analysis", use_container_width=True, type="primary"):
        st.switch_page("pages/Analyze_Audio.py")

with col2:
    if st.button("📊 Explore Analytics Dashboard", use_container_width=True):
        st.switch_page("pages/Dashboard.py")

st.markdown("<hr>", unsafe_allow_html=True)

# ---------------------------------
# Key Features
# ---------------------------------

st.markdown("### ✨ Intelligent Assessment Features")
st.caption("Comprehensive AI architecture designed for authentic conceptual evaluation")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎙️</div>
        <div class="feature-title">High-Accuracy Speech-to-Text</div>
        <div class="feature-description">
            Converts technical audio explanations into precise transcripts using Faster Whisper
            optimized for diverse accents, technical jargon, and speaking cadences.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🧠</div>
        <div class="feature-title">Deep Semantic Matching</div>
        <div class="feature-description">
            Goes beyond surface word-matching. Uses Sentence-BERT embeddings to evaluate whether
            the student truly understands the underlying concept and its principles.
        </div>
    </div>
    """, unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <div class="feature-title">Multi-Dimensional Scoring</div>
        <div class="feature-description">
            Quantifies concept accuracy, explanation depth, keyword presence, and speech metrics
            (duration, words per minute, loudness, and silence ratio).
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📑</div>
        <div class="feature-title">Automated PDF Verification</div>
        <div class="feature-description">
            Instantly generates downloadable, structured PDF reports complete with score breakdowns,
            personalized AI feedback, and learning recommendations.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ---------------------------------
# How It Works
# ---------------------------------

st.markdown("### ⚙️ How The Assessment Works")
st.caption("Four simple steps from spoken explanation to verified assessment report")

step1, step2, step3, step4 = st.columns(4)

with step1:
    st.markdown("""
    <div class="workflow-card">
        <div class="workflow-step-num">1</div>
        <h4>Record & Upload</h4>
        <p>Record your voice explaining a technical concept and upload in WAV, MP3, M4A, or OGG format.</p>
    </div>
    """, unsafe_allow_html=True)

with step2:
    st.markdown("""
    <div class="workflow-card">
        <div class="workflow-step-num">2</div>
        <h4>Speech Transcription</h4>
        <p>Faster Whisper extracts acoustic features and generates high-fidelity textual transcriptions.</p>
    </div>
    """, unsafe_allow_html=True)

with step3:
    st.markdown("""
    <div class="workflow-card">
        <div class="workflow-step-num">3</div>
        <h4>Semantic AI Evaluation</h4>
        <p>Sentence-BERT models compare explanation embeddings with verified expert reference knowledge.</p>
    </div>
    """, unsafe_allow_html=True)

with step4:
    st.markdown("""
    <div class="workflow-card">
        <div class="workflow-step-num">4</div>
        <h4>Instant Report & PDF</h4>
        <p>Review comprehensive scores, keyword analysis, AI suggestions, and download the official PDF.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ---------------------------------
# AI Processing Pipeline
# ---------------------------------

st.markdown("### 🧠 AI Processing Pipeline")
st.caption("Real-time end-to-end evaluation dataflow")

c1, a1, c2, a2, c3, a3, c4, a4, c5, a5, c6 = st.columns([2, 0.4, 2, 0.4, 2, 0.4, 2, 0.4, 2, 0.4, 2])

with c1:
    st.markdown("""
    <div class="pipeline-card">
        <div class="pipeline-icon">🎤</div>
        <h4>Voice Input</h4>
        <p>User audio upload</p>
    </div>
    """, unsafe_allow_html=True)

with a1:
    st.markdown("<h3 class='pipeline-arrow'>➜</h3>", unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="pipeline-card">
        <div class="pipeline-icon">🎙️</div>
        <h4>ASR Engine</h4>
        <p>Faster Whisper</p>
    </div>
    """, unsafe_allow_html=True)

with a2:
    st.markdown("<h3 class='pipeline-arrow'>➜</h3>", unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="pipeline-card">
        <div class="pipeline-icon">📝</div>
        <h4>Transcript</h4>
        <p>Cleaned speech text</p>
    </div>
    """, unsafe_allow_html=True)

with a3:
    st.markdown("<h3 class='pipeline-arrow'>➜</h3>", unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="pipeline-card">
        <div class="pipeline-icon">🧠</div>
        <h4>Embeddings</h4>
        <p>Sentence-BERT</p>
    </div>
    """, unsafe_allow_html=True)

with a4:
    st.markdown("<h3 class='pipeline-arrow'>➜</h3>", unsafe_allow_html=True)

with c5:
    st.markdown("""
    <div class="pipeline-card">
        <div class="pipeline-icon">📊</div>
        <h4>Scoring & NLP</h4>
        <p>Keywords & Speech</p>
    </div>
    """, unsafe_allow_html=True)

with a5:
    st.markdown("<h3 class='pipeline-arrow'>➜</h3>", unsafe_allow_html=True)

with c6:
    st.markdown("""
    <div class="pipeline-card">
        <div class="pipeline-icon">📑</div>
        <h4>PDF & Insights</h4>
        <p>Verified Report</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ---------------------------------
# Project Highlights
# ---------------------------------

st.markdown("### 📈 Core Architecture Highlights")
st.caption("Key technical metrics and foundational capabilities")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="highlight-card">
        <div class="highlight-icon">🤖</div>
        <h3>AI Foundation</h3>
        <div class="highlight-value">2 Models</div>
        <p>Faster Whisper ASR<br>Sentence-BERT Embeddings</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="highlight-card">
        <div class="highlight-icon">📚</div>
        <h3>Preloaded Domains</h3>
        <div class="highlight-value">6 Topics</div>
        <p>ML, Cloud, AI, Data Science, DBMS & Operating Systems</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="highlight-card">
        <div class="highlight-icon">⚡</div>
        <h3>Analysis Speed</h3>
        <div class="highlight-value">&lt; 3 Sec</div>
        <p>Instant GPU/CPU inference with detailed acoustic metrics</p>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="highlight-card">
        <div class="highlight-icon">💾</div>
        <h3>Persistence</h3>
        <div class="highlight-value">SQLite DB</div>
        <p>Historical audit trails, analytics, and instant retrieval</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ---------------------------------
# Supported Topics
# ---------------------------------

st.markdown("### 📚 Supported Technical Topics")
st.caption("Standardized expert reference knowledge bases")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="topic-card">
        <div class="topic-icon">🤖</div>
        <h3>Artificial Intelligence & ML</h3>
        <p>
            • <strong>Machine Learning:</strong> Supervised, unsupervised, reinforcement learning.<br>
            • <strong>Artificial Intelligence:</strong> Neural nets, heuristics, autonomous reasoning.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="topic-card">
        <div class="topic-icon">☁️</div>
        <h3>Systems & Infrastructure</h3>
        <p>
            • <strong>Cloud Computing:</strong> IaaS, PaaS, SaaS, virtualization, scaling.<br>
            • <strong>Operating Systems:</strong> Processes, memory management, scheduling.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="topic-card">
        <div class="topic-icon">💾</div>
        <h3>Data & Storage</h3>
        <p>
            • <strong>DBMS:</strong> Relational design, ACID properties, normalization.<br>
            • <strong>Data Science:</strong> EDA, statistical inference, feature engineering.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ---------------------------------
# Why Choose VBCUA
# ---------------------------------

st.markdown("### 🌟 Value For Learners & Educators")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="choose-card">
        <div class="choose-icon">🎓</div>
        <h3>For Students & Job Seekers</h3>
        <p>
            ✔ Master technical interview explanations by practicing out loud.<br>
            ✔ Get objective AI feedback on concept completeness & clarity.<br>
            ✔ Discover missing critical technical keywords automatically.<br>
            ✔ Build confidence and track your skill progression over time.<br>
            ✔ Download verifiable PDF reports for your skill portfolio.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="choose-card">
        <div class="choose-icon">👨‍🏫</div>
        <h3>For Educators & Assessors</h3>
        <p>
            ✔ Automate oral viva examinations with zero grading fatigue.<br>
            ✔ Evaluate semantic comprehension instead of rote memorization.<br>
            ✔ View holistic cohort performance on the analytics dashboard.<br>
            ✔ Maintain auditable, persistent evaluation records in SQLite.<br>
            ✔ Export CSV datasets for academic and institutional research.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ---------------------------------
# Footer
# ---------------------------------

st.markdown("""
<div class="footer">
    <h2>SkillWallet • Voice-Based Concept Understanding Analyser</h2>
    <p class="footer-subtitle">
        AI-Powered Educational Assessment Platform & Conceptual Intelligence
    </p>
    <div class="footer-grid">
        <div class="footer-box">
            <h4>🛠 Technologies</h4>
            <p>
                Python 3.13 • Streamlit • Faster-Whisper ASR<br>
                Sentence-BERT Embeddings • Librosa Acoustic NLP<br>
                Plotly Analytics • ReportLab PDF Engine
            </p>
        </div>
        <div class="footer-box">
            <h4>⚡ Assessment Capabilities</h4>
            <p>
                Speech-to-Text Transcription • Semantic Vector Scoring<br>
                Technical Keyword Coverage • Pacing & Audio Metrics<br>
                Instant Downloadable PDF Reports
            </p>
        </div>
        <div class="footer-box">
            <h4>🎯 Mission</h4>
            <p>
                Bridging the gap between knowledge retention and expressive mastery
                through conversational AI and deep learning.
            </p>
        </div>
    </div>
    <div class="copyright">
        © 2026 SkillWallet AI • Major Project Assessment Engine • Built with Generative AI & Streamlit
    </div>
</div>
""", unsafe_allow_html=True)
