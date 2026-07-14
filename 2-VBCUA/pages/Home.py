from pathlib import Path
import streamlit as st

# ---------------------------------
# Load CSS
# ---------------------------------

def load_css():
    css_path = Path(__file__).parent.parent / "assets" / "styles" / "custom.css"

    if css_path.exists():
        with open(css_path, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ---------------------------------
# Page Configuration
# ---------------------------------

st.set_page_config(
    page_title="Voice-Based Concept Understanding Analyser",
    page_icon="🎤",
    layout="wide"
)

# ---------------------------------
# Hero Section
# ---------------------------------

st.title("🎤 Voice-Based Concept Understanding Analyser")

st.caption("AI-Powered Educational Assessment Platform")

st.markdown("---")

st.markdown(
    """
<div class="hero-card">
    <h1>Welcome to VBCUA</h1>

<p style="font-size:18px;">
Voice-Based Concept Understanding Analyser (VBCUA) is an intelligent
educational assessment system that evaluates a student's conceptual
understanding through speech. It converts spoken explanations into text,
compares them with expert reference concepts using Artificial Intelligence,
and generates detailed feedback with downloadable PDF reports.
</p>

</div>
""",
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "🚀 Start Analysis",
        use_container_width=True
    ):
        st.switch_page("pages/Analyze_Audio.py")

with col2:

    if st.button(
        "📊 Dashboard",
        use_container_width=True
    ):
        st.switch_page("pages/Dashboard.py")

st.markdown("---")


st.markdown("---")

# ---------------------------------
# Key Features
# ---------------------------------

st.header("✨ Key Features")

col1, col2 = st.columns(2)

with col1:

    st.markdown(
        """
<div class="feature-card">

<div class="feature-icon">🎙️</div>

<div class="feature-title">
Speech-to-Text
</div>

<div class="feature-description">
Convert spoken explanations into accurate text using Faster Whisper.
</div>

</div>
""",
        unsafe_allow_html=True,
    )

with col2:

    st.markdown(
        """
<div class="feature-card">

<div class="feature-icon">🧠</div>

<div class="feature-title">
Semantic Similarity
</div>

<div class="feature-description">
Compare student explanations with reference concepts using Sentence-BERT.
</div>

</div>
""",
        unsafe_allow_html=True,
    )

col3, col4 = st.columns(2)

with col3:

    st.markdown(
        """
<div class="feature-card">

<div class="feature-icon">📊</div>

<div class="feature-title">
Performance Analysis
</div>

<div class="feature-description">
Evaluate conceptual accuracy, explanation quality, keyword matching, and overall understanding.
</div>

</div>
""",
        unsafe_allow_html=True,
    )

with col4:

    st.markdown(
        """
<div class="feature-card">

<div class="feature-icon">📄</div>

<div class="feature-title">
PDF Reports
</div>

<div class="feature-description">
Generate downloadable PDF reports containing scores, feedback, transcript, and analysis results.
</div>

</div>
""",
        unsafe_allow_html=True,
    )

st.markdown("---")


# ---------------------------------
# How It Works
# ---------------------------------

st.header("⚙️ How It Works")

step1, step2, step3, step4 = st.columns(4)

with step1:

    st.markdown("""
<div class="workflow-card">

<h2>1️⃣</h2>

<h4>Upload Audio</h4>

<p>
Upload your recorded voice explanation to begin the AI-powered analysis.
</p>

</div>
""", unsafe_allow_html=True)

with step2:

    st.markdown("""
<div class="workflow-card">

<h2>2️⃣</h2>

<h4>Speech Recognition</h4>

<p>
Faster Whisper converts the uploaded speech into accurate text.
</p>

</div>
""", unsafe_allow_html=True)

with step3:

    st.markdown("""
<div class="workflow-card">

<h2>3️⃣</h2>

<h4>AI Analysis</h4>

<p>
Sentence-BERT compares the explanation with the reference concept and evaluates understanding.
</p>

</div>
""", unsafe_allow_html=True)

with step4:

    st.markdown("""
<div class="workflow-card">

<h2>4️⃣</h2>

<h4>Results & Report</h4>

<p>
View scores, feedback, keyword matching and download the professional PDF report.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------------------------
# Technologies Used
# ---------------------------------

st.header("🛠 Technologies Used")

tech1, tech2, tech3 = st.columns(3)

with tech1:

    st.markdown("""
<div class="tech-card">

<div class="tech-icon">🐍</div>

<h3>Programming</h3>

<p>

✔ Python<br>

✔ Streamlit<br>

✔ SQLite

</p>

</div>
""", unsafe_allow_html=True)

with tech2:

    st.markdown("""
<div class="tech-card">

<div class="tech-icon">🤖</div>

<h3>Artificial Intelligence</h3>

<p>

✔ Faster Whisper<br>

✔ Sentence-BERT<br>

✔ Transformers

</p>

</div>
""", unsafe_allow_html=True)

with tech3:

    st.markdown("""
<div class="tech-card">

<div class="tech-icon">📚</div>

<h3>Libraries</h3>

<p>

✔ Torch<br>

✔ Librosa<br>

✔ Plotly<br>

✔ ReportLab<br>

✔ Pandas

</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------------------------
# Project Highlights
# ---------------------------------

st.header("📈 Project Highlights")

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.markdown("""
<div class="highlight-card">

<div class="highlight-icon">🤖</div>

<h3>AI Models</h3>

<div class="highlight-value">2</div>

<p>

Faster Whisper<br>

Sentence-BERT

</p>

</div>
""", unsafe_allow_html=True)

with c2:

    st.markdown("""
<div class="highlight-card">

<div class="highlight-icon">📚</div>

<h3>Topics</h3>

<div class="highlight-value">6</div>

<p>

Machine Learning<br>

Cloud Computing<br>

Artificial Intelligence<br>

Data Science<br>

DBMS<br>

Operating System

</p>

</div>
""", unsafe_allow_html=True)

with c3:

    st.markdown("""
<div class="highlight-card">

<div class="highlight-icon">📄</div>

<h3>Reports</h3>

<div class="highlight-value">PDF</div>

<p>

Transcript<br>

Scores<br>

AI Feedback<br>

Keyword Analysis

</p>

</div>
""", unsafe_allow_html=True)

with c4:

    st.markdown("""
<div class="highlight-card">

<div class="highlight-icon">💾</div>

<h3>Database</h3>

<div class="highlight-value">SQLite</div>

<p>

Stores analysis history<br>

Tracks reports<br>

Maintains results

</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")
# ---------------------------------
# Why Choose VBCUA
# ---------------------------------

st.header("🌟 Why Choose VBCUA")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
<div class="choose-card">

<div class="choose-icon">🎓</div>

<h3>For Students</h3>

<p>

✔ Improve conceptual understanding<br><br>

✔ Practice explaining concepts confidently<br><br>

✔ Receive instant AI-generated feedback<br><br>

✔ Identify missing concepts and keywords<br><br>

✔ Download professional PDF reports

</p>

</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="choose-card">

<div class="choose-icon">👨‍🏫</div>

<h3>For Educators</h3>

<p>

✔ Evaluate conceptual understanding quickly<br><br>

✔ Save manual assessment time<br><br>

✔ Review AI-generated analysis reports<br><br>

✔ Track student performance efficiently<br><br>

✔ Maintain complete assessment history

</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")


# ---------------------------------
# Supported Topics
# ---------------------------------

st.header("📚 Supported Topics")

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
<div class="topic-card">

<div class="topic-icon">🤖</div>

<h3>Artificial Intelligence</h3>

<p>

✔ Machine Learning<br><br>

✔ Artificial Intelligence

</p>

</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="topic-card">

<div class="topic-icon">☁️</div>

<h3>Computing</h3>

<p>

✔ Cloud Computing<br><br>

✔ Operating System

</p>

</div>
""", unsafe_allow_html=True)

with col3:

    st.markdown("""
<div class="topic-card">

<div class="topic-icon">💾</div>

<h3>Data Management</h3>

<p>

✔ Database Management System<br><br>

✔ Data Science

</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------------------------
# Future Enhancements
# ---------------------------------

st.header("🚀 Future Enhancements")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
<div class="future-card">

<div class="future-icon">🎤</div>

<h3>Advanced AI Features</h3>

<p>

✔ Live Voice Recording<br><br>

✔ Multi-language Speech Recognition<br><br>

✔ AI Conversation Practice<br><br>

✔ Voice Emotion Detection<br><br>

✔ Personalized Learning Suggestions

</p>

</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="future-card">

<div class="future-icon">☁️</div>

<h3>Platform Enhancements</h3>

<p>

✔ Student Login & Authentication<br><br>

✔ Teacher Dashboard<br><br>

✔ Cloud Deployment<br><br>

✔ Progress Tracking<br><br>

✔ Mobile Responsive Application

</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")



# ---------------------------------
# AI Processing Pipeline
# ---------------------------------

st.header("🧠 AI Processing Pipeline")

c1, a1, c2, a2, c3, a3, c4, a4, c5, a5, c6 = st.columns(
    [2, 0.4, 2, 0.4, 2, 0.4, 2, 0.4, 2, 0.4, 2]
)

with c1:
    st.markdown("""
<div class="pipeline-card">

<div class="pipeline-icon">🎤</div>

<h4>Voice Input</h4>

<p>
Upload audio
</p>

</div>
""", unsafe_allow_html=True)

with a1:
    st.markdown("<h1 class='pipeline-arrow'>➜</h1>", unsafe_allow_html=True)

with c2:
    st.markdown("""
<div class="pipeline-card">

<div class="pipeline-icon">🎙️</div>

<h4>Speech Recognition</h4>

<p>
Faster Whisper
</p>

</div>
""", unsafe_allow_html=True)

with a2:
    st.markdown("<h1 class='pipeline-arrow'>➜</h1>", unsafe_allow_html=True)

with c3:
    st.markdown("""
<div class="pipeline-card">

<div class="pipeline-icon">📝</div>

<h4>Transcript</h4>

<p>
Speech converted
to text
</p>

</div>
""", unsafe_allow_html=True)

with a3:
    st.markdown("<h1 class='pipeline-arrow'>➜</h1>", unsafe_allow_html=True)

with c4:
    st.markdown("""
<div class="pipeline-card">

<div class="pipeline-icon">🧠</div>

<h4>Semantic Analysis</h4>

<p>
Sentence-BERT
</p>

</div>
""", unsafe_allow_html=True)

with a4:
    st.markdown("<h1 class='pipeline-arrow'>➜</h1>", unsafe_allow_html=True)

with c5:
    st.markdown("""
<div class="pipeline-card">

<div class="pipeline-icon">📊</div>

<h4>Scoring</h4>

<p>
Keyword Matching
&
Audio Analysis
</p>

</div>
""", unsafe_allow_html=True)

with a5:
    st.markdown("<h1 class='pipeline-arrow'>➜</h1>", unsafe_allow_html=True)

with c6:
    st.markdown("""
<div class="pipeline-card">

<div class="pipeline-icon">📄</div>

<h4>Report</h4>

<p>
Feedback &
PDF Report
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------------------------
# Footer
# ---------------------------------

st.markdown("---")

st.markdown("""
<div class="footer">

<h2>🎤 Voice-Based Concept Understanding Analyser</h2>

<p class="footer-subtitle">
AI-Powered Educational Assessment Platform
</p>

<div class="footer-grid">

<div class="footer-box">

<h4>🛠 Technologies</h4>

<p>

Python<br>
Streamlit<br>
Faster Whisper<br>
Sentence-BERT<br>
SQLite<br>
Plotly

</p>

</div>

<div class="footer-box">

<h4>📚 Features</h4>

<p>

Speech-to-Text<br>
Semantic Similarity<br>
Keyword Matching<br>
Audio Statistics<br>
PDF Reports

</p>

</div>

<div class="footer-box">

<h4>🎯 Purpose</h4>

<p>

Evaluate conceptual understanding using Artificial Intelligence and generate instant performance feedback.

</p>

</div>

</div>

<hr>

<p class="copyright">

© 2026 Voice-Based Concept Understanding Analyser (VBCUA)<br>

Developed using Python, Streamlit and Artificial Intelligence.

</p>

</div>
""", unsafe_allow_html=True)


