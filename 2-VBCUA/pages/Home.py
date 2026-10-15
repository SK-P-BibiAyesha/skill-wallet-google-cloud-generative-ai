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

features_html = "".join(
    f"""
    <div class="feature-card">
        <div class="feature-icon">{icon}</div>
        <h3 class="feature-title">{title}</h3>
        <p class="feature-description">{desc}</p>
    </div>
    """
    for icon, title, desc in features
)
st.markdown(f'<div class="vbcua-grid vbcua-grid-4">{features_html}</div>', unsafe_allow_html=True)

st.divider()

# -------------------------------------------------------------------
# How It Works
# -------------------------------------------------------------------
st.header("⚙️ How It Works")
workflow = [
    ("01", "Upload Audio",
     "Upload your recorded voice explanation to begin the AI-powered analysis."),
    ("02", "Speech Recognition",
     "Faster Whisper converts the uploaded speech into accurate text."),
    ("03", "AI Analysis",
     "Sentence-BERT compares the explanation with the reference concept and evaluates understanding."),
    ("04", "Results & Report",
     "View scores, feedback, keyword matching and download the professional PDF report."),
]

workflow_html = "".join(
    f"""
    <div class="how-card">
        <div class="how-number">{number}</div>
        <h4 class="how-title">{title}</h4>
        <p class="how-description">{desc}</p>
    </div>
    """
    for number, title, desc in workflow
)
st.markdown(f'<div class="vbcua-grid vbcua-grid-4">{workflow_html}</div>', unsafe_allow_html=True)

st.divider()

# -------------------------------------------------------------------
# Technologies Used
# -------------------------------------------------------------------
st.header("🛠 Technologies Used")
technologies = [
    ("🐍", "Application", ["Python", "Streamlit"]),
    ("🤖", "AI Models", ["Faster Whisper", "Sentence-BERT", "Transformers"]),
    ("📚", "Supporting Libraries", ["SQLite", "ReportLab", "Librosa", "Plotly", "Pandas"]),
]

tech_html = "".join(
    f"""
    <div class="tech-card">
        <div class="tech-header">
            <span class="tech-icon">{icon}</span>
            <h3 class="tech-title">{title}</h3>
        </div>
        <div class="tech-list">
            {"".join(f'<span class="tech-pill">{item}</span>' for item in items)}
        </div>
    </div>
    """
    for icon, title, items in technologies
)
st.markdown(f'<div class="vbcua-grid vbcua-grid-3">{tech_html}</div>', unsafe_allow_html=True)

st.divider()

# -------------------------------------------------------------------
# Project Highlights
# -------------------------------------------------------------------
st.header("📈 Project Highlights")
highlights = [
    ("🤖", "AI Models", "2", ["Faster Whisper", "Sentence-BERT"]),
    ("📚", "Topics", "6", [
        "Machine Learning",
        "Cloud Computing",
        "Artificial Intelligence",
        "Data Science",
        "DBMS",
        "Operating System",
    ]),
    ("📄", "Reports", "PDF", ["Transcript", "Scores", "AI Feedback", "Keyword Analysis"]),
    ("💾", "Database", "SQLite", ["Stores analysis history", "Tracks reports", "Maintains results"]),
]

highlights_html = "".join(
    f"""
    <div class="highlight-card">
        <div class="highlight-top">
            <span class="highlight-icon">{icon}</span>
            <h3 class="highlight-title">{title}</h3>
        </div>
        <div class="highlight-value-badge">{val}</div>
        <div class="highlight-items">
            {"".join(f'<span class="highlight-chip">{item}</span>' for item in items)}
        </div>
    </div>
    """
    for icon, title, val, items in highlights
)
st.markdown(f'<div class="vbcua-grid vbcua-grid-4">{highlights_html}</div>', unsafe_allow_html=True)

st.divider()

# -------------------------------------------------------------------
# Why Choose VBCUA
# -------------------------------------------------------------------
st.header("🌟 Why Choose VBCUA")
choices = [
    (
        "🎓",
        "For Students",
        [
            "Improve conceptual understanding",
            "Practice explaining concepts confidently",
            "Receive instant AI-generated feedback",
            "Identify missing concepts and keywords",
            "Download professional PDF reports",
        ],
    ),
    (
        "👨‍🏫",
        "For Educators",
        [
            "Evaluate conceptual understanding quickly",
            "Save manual assessment time",
            "Review AI-generated analysis reports",
            "Track student performance efficiently",
            "Maintain complete assessment history",
        ],
    ),
]

choose_html = "".join(
    f"""
    <div class="choose-card">
        <div class="choose-header">
            <span class="choose-icon">{icon}</span>
            <h3 class="choose-title">{title}</h3>
        </div>
        <div class="choose-list">
            {"".join(f'<div class="choose-item">{point}</div>' for point in points)}
        </div>
    </div>
    """
    for icon, title, points in choices
)
st.markdown(f'<div class="vbcua-grid vbcua-grid-2">{choose_html}</div>', unsafe_allow_html=True)

st.divider()

# -------------------------------------------------------------------
# Supported Topics
# -------------------------------------------------------------------
st.header("📚 Supported Topics")
topics = [
    ("🤖", "Artificial Intelligence", ["Machine Learning", "Artificial Intelligence"]),
    ("☁️", "Computing", ["Cloud Computing", "Operating System"]),
    ("💾", "Data Management", ["Database Management System", "Data Science"]),
]

topics_html = "".join(
    f"""
    <div class="topic-card">
        <div class="topic-header">
            <span class="topic-icon">{icon}</span>
            <h3 class="topic-title">{title}</h3>
        </div>
        <div class="topic-list">
            {"".join(f'<div class="topic-pill">{item}</div>' for item in items)}
        </div>
    </div>
    """
    for icon, title, items in topics
)
st.markdown(f'<div class="vbcua-grid vbcua-grid-3">{topics_html}</div>', unsafe_allow_html=True)

st.divider()

# -------------------------------------------------------------------
# Future Enhancements
# -------------------------------------------------------------------
st.header("🚀 Future Enhancements")
future = [
    (
        "🎤",
        "Advanced AI Features",
        [
            "Live Voice Recording",
            "Multi-language Speech Recognition",
            "AI Conversation Practice",
            "Voice Emotion Detection",
            "Personalized Learning Suggestions",
        ],
    ),
    (
        "☁️",
        "Platform Enhancements",
        [
            "Student Login & Authentication",
            "Teacher Dashboard",
            "Cloud Deployment",
            "Progress Tracking",
            "Mobile Responsive Application",
        ],
    ),
]

future_html = "".join(
    f"""
    <div class="future-card">
        <div class="future-header">
            <span class="future-icon">{icon}</span>
            <h3 class="future-title">{title}</h3>
        </div>
        <div class="future-list">
            {"".join(f'<div class="future-item">{point}</div>' for point in points)}
        </div>
    </div>
    """
    for icon, title, points in future
)
st.markdown(f'<div class="vbcua-grid vbcua-grid-2">{future_html}</div>', unsafe_allow_html=True)

st.divider()

# -------------------------------------------------------------------
# AI Processing Pipeline
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

pipeline_html = "".join(
    f"""
    <div class="pipeline-card">
        <div class="pipeline-top">
            <span class="pipeline-icon">{icon}</span>
            <span class="pipeline-stage">Stage 0{i + 1}</span>
        </div>
        <h4 class="pipeline-title">{title}</h4>
        <p class="pipeline-description">{desc}</p>
    </div>
    """
    for i, (icon, title, desc) in enumerate(pipeline)
)
st.markdown(f'<div class="vbcua-grid vbcua-grid-pipeline">{pipeline_html}</div>', unsafe_allow_html=True)

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
