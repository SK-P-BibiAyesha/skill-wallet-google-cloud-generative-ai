import streamlit as st
from utils.helper import load_css

# Page configuration is managed by app.py via st.navigation().
load_css()

# -------------------------------------------------------------------
# Hero
# -------------------------------------------------------------------
st.title("VBCUA")
st.caption("Voice-Based Concept Understanding Analyser · AI-Powered Educational Assessment Platform")
st.divider()

st.markdown(
    """
    <section class="hero-card">
        <h2>Learn by explaining concepts aloud.</h2>
        <p>
            Voice-Based Concept Understanding Analyser (VBCUA) is an
            intelligent educational assessment system that evaluates a
            student's conceptual understanding through speech. It converts
            spoken explanations into text, compares them with expert reference
            concepts using Artificial Intelligence, and generates detailed
            feedback with downloadable PDF reports.
        </p>
        <div class="hero-badges">
            <span>🎙️ Faster Whisper</span>
            <span>🧠 Sentence-BERT</span>
            <span>📊 Similarity-Based Scoring</span>
            <span>📄 PDF Reports</span>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

action1, action2 = st.columns(2)
with action1:
    if st.button("🚀 Start Analysis", width="stretch", type="primary"):
        st.switch_page("pages/Analyze_Audio.py")
with action2:
    if st.button("📊 Dashboard", width="stretch"):
        st.switch_page("pages/Dashboard.py")

st.divider()

# -------------------------------------------------------------------
# Key Features
# -------------------------------------------------------------------
st.header("✨ Key Features")
features = [
    ("🎙️", "Speech-to-Text",
     "Convert spoken explanations into accurate text using Faster Whisper."),
    ("🧠", "Semantic Similarity",
     "Compare student explanations with reference concepts using Sentence-BERT."),
    ("📊", "Performance Analysis",
     "Evaluate conceptual accuracy, explanation quality, keyword matching, and overall understanding."),
    ("📄", "PDF Reports",
     "Generate downloadable PDF reports containing scores, feedback, transcript, and analysis results."),
]
for i in range(0, len(features), 2):
    columns = st.columns(2)
    for col, (icon, title, description) in zip(columns, features[i:i + 2]):
        with col:
            st.markdown(
                f"""
                <div class="feature-card">
                    <div class="feature-icon">{icon}</div>
                    <h3 class="feature-title">{title}</h3>
                    <p class="feature-description">{description}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

st.divider()

# -------------------------------------------------------------------
# How It Works
# -------------------------------------------------------------------
st.header("⚙️ How It Works")
workflow = [
    ("1️⃣", "Upload Audio",
     "Upload your recorded voice explanation to begin the AI-powered analysis."),
    ("2️⃣", "Speech Recognition",
     "Faster Whisper converts the uploaded speech into accurate text."),
    ("3️⃣", "AI Analysis",
     "Sentence-BERT compares the explanation with the reference concept and evaluates understanding."),
    ("4️⃣", "Results & Report",
     "View scores, feedback, keyword matching and download the professional PDF report."),
]
for i in range(0, len(workflow), 2):
    columns = st.columns(2)
    for col, (number, title, description) in zip(columns, workflow[i:i + 2]):
        with col:
            st.markdown(
                f"""
                <div class="workflow-card">
                    <div class="workflow-number">{number}</div>
                    <h4>{title}</h4>
                    <p>{description}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

st.divider()

# -------------------------------------------------------------------
# Technologies Used
# -------------------------------------------------------------------
st.header("🛠 Technologies Used")
technologies = [
    ("🐍", "Programming", "✔ Python<br>✔ Streamlit<br>✔ SQLite"),
    ("🤖", "Artificial Intelligence",
     "✔ Faster Whisper<br>✔ Sentence-BERT<br>✔ Transformers"),
    ("📚", "Libraries",
     "✔ Torch<br>✔ Librosa<br>✔ Plotly<br>✔ ReportLab<br>✔ Pandas"),
]
columns = st.columns(3)
for col, (icon, title, items) in zip(columns, technologies):
    with col:
        st.markdown(
            f"""
            <div class="tech-card">
                <div class="tech-icon">{icon}</div>
                <h3>{title}</h3>
                <p>{items}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.divider()

# -------------------------------------------------------------------
# Project Highlights
# -------------------------------------------------------------------
st.header("📈 Project Highlights")
highlights = [
    ("🤖", "AI Models", "2", "Faster Whisper<br>Sentence-BERT"),
    ("📚", "Topics", "6",
     "Machine Learning<br>Cloud Computing<br>Artificial Intelligence<br>"
     "Data Science<br>DBMS<br>Operating System"),
    ("📄", "Reports", "PDF",
     "Transcript<br>Scores<br>AI Feedback<br>Keyword Analysis"),
    ("💾", "Database", "SQLite",
     "Stores analysis history<br>Tracks reports<br>Maintains results"),
]
for i in range(0, len(highlights), 2):
    columns = st.columns(2)
    for col, (icon, title, value, details) in zip(columns, highlights[i:i + 2]):
        with col:
            st.markdown(
                f"""
                <div class="highlight-card">
                    <div class="highlight-icon">{icon}</div>
                    <h3>{title}</h3>
                    <div class="highlight-value">{value}</div>
                    <p>{details}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

st.divider()

# -------------------------------------------------------------------
# Why Choose VBCUA
# -------------------------------------------------------------------
st.header("🌟 Why Choose VBCUA")
choices = [
    ("🎓", "For Students",
     "✔ Improve conceptual understanding<br><br>"
     "✔ Practice explaining concepts confidently<br><br>"
     "✔ Receive instant AI-generated feedback<br><br>"
     "✔ Identify missing concepts and keywords<br><br>"
     "✔ Download professional PDF reports"),
    ("👨‍🏫", "For Educators",
     "✔ Evaluate conceptual understanding quickly<br><br>"
     "✔ Save manual assessment time<br><br>"
     "✔ Review AI-generated analysis reports<br><br>"
     "✔ Track student performance efficiently<br><br>"
     "✔ Maintain complete assessment history"),
]
columns = st.columns(2)
for col, (icon, title, details) in zip(columns, choices):
    with col:
        st.markdown(
            f"""
            <div class="choose-card">
                <div class="choose-icon">{icon}</div>
                <h3>{title}</h3>
                <p>{details}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.divider()

# -------------------------------------------------------------------
# Supported Topics
# -------------------------------------------------------------------
st.header("📚 Supported Topics")
topics = [
    ("🤖", "Artificial Intelligence",
     "✔ Machine Learning<br><br>✔ Artificial Intelligence"),
    ("☁️", "Computing",
     "✔ Cloud Computing<br><br>✔ Operating System"),
    ("💾", "Data Management",
     "✔ Database Management System<br><br>✔ Data Science"),
]
columns = st.columns(3)
for col, (icon, title, details) in zip(columns, topics):
    with col:
        st.markdown(
            f"""
            <div class="topic-card">
                <div class="topic-icon">{icon}</div>
                <h3>{title}</h3>
                <p>{details}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.divider()

# -------------------------------------------------------------------
# Future Enhancements
# -------------------------------------------------------------------
st.header("🚀 Future Enhancements")
future = [
    ("🎤", "Advanced AI Features",
     "✔ Live Voice Recording<br><br>"
     "✔ Multi-language Speech Recognition<br><br>"
     "✔ AI Conversation Practice<br><br>"
     "✔ Voice Emotion Detection<br><br>"
     "✔ Personalized Learning Suggestions"),
    ("☁️", "Platform Enhancements",
     "✔ Student Login & Authentication<br><br>"
     "✔ Teacher Dashboard<br><br>"
     "✔ Cloud Deployment<br><br>"
     "✔ Progress Tracking<br><br>"
     "✔ Mobile Responsive Application"),
]
columns = st.columns(2)
for col, (icon, title, details) in zip(columns, future):
    with col:
        st.markdown(
            f"""
            <div class="future-card">
                <div class="future-icon">{icon}</div>
                <h3>{title}</h3>
                <p>{details}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.divider()

# -------------------------------------------------------------------
# AI Processing Pipeline
# Important: no separate arrow columns. This is a 3 x 2 card grid.
# -------------------------------------------------------------------
st.header("🧠 AI Processing Pipeline")
pipeline = [
    ("🎤", "Voice Input", "Upload audio"),
    ("🎙️", "Speech Recognition", "Faster Whisper"),
    ("📝", "Transcript", "Speech converted to text"),
    ("🧠", "Semantic Analysis", "Sentence-BERT"),
    ("📊", "Scoring", "Keyword Matching & Audio Analysis"),
    ("📄", "Report", "Feedback & PDF Report"),
]
for i in range(0, len(pipeline), 3):
    columns = st.columns(3)
    for col, (icon, title, description) in zip(columns, pipeline[i:i + 3]):
        with col:
            st.markdown(
                f"""
                <div class="pipeline-card">
                    <div class="pipeline-icon">{icon}</div>
                    <h4>{title}</h4>
                    <p>{description}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

st.divider()

# -------------------------------------------------------------------
# Footer
# -------------------------------------------------------------------
st.markdown(
    """
    <footer class="footer">
        <h2>🎤 Voice-Based Concept Understanding Analyser</h2>
        <p class="footer-subtitle">AI-Powered Educational Assessment Platform</p>
        <div class="footer-grid">
            <div class="footer-box">
                <h4>🛠 Technologies</h4>
                <p>Python<br>Streamlit<br>Faster Whisper<br>Sentence-BERT<br>SQLite<br>Plotly</p>
            </div>
            <div class="footer-box">
                <h4>📚 Features</h4>
                <p>Speech-to-Text<br>Semantic Similarity<br>Keyword Matching<br>Audio Statistics<br>PDF Reports</p>
            </div>
            <div class="footer-box">
                <h4>🎯 Purpose</h4>
                <p>Compare spoken explanations with reference concepts and present analysis scores and feedback.</p>
            </div>
        </div>
        <hr>
        <p class="copyright">
            © 2026 Voice-Based Concept Understanding Analyser (VBCUA)<br>
            Developed using Python, Streamlit and Artificial Intelligence.
        </p>
    </footer>
    """,
    unsafe_allow_html=True,
)
