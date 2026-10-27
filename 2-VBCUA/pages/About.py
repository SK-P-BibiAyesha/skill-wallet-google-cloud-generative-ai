import streamlit as st
from utils.helper import load_css

load_css()

st.title("ℹ️ About VBCUA")
st.caption("A voice-based educational assessment platform.")
st.divider()

st.markdown(
    """
    <div class="vbcua-card" style="margin-bottom: 1.5rem;">
        <h3 style="margin-top: 0; color: var(--vbcua-navy); font-size: 1.25rem;">🎤 Voice-Based Concept Understanding Analyser</h3>
        <p style="margin: 0; color: var(--vbcua-text); line-height: 1.7;">
            The Voice-Based Concept Understanding Analyser (VBCUA) evaluates a
            student's conceptual understanding through spoken explanations.
            Instead of checking only for exact words, it compares the explanation's
            semantic meaning with a reference concept using Artificial Intelligence.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# -------------------------------------------------------------------
# Features
# -------------------------------------------------------------------
st.header("✨ Features")
features = [
    ("🎤", "Audio Upload", "Upload a spoken explanation for analysis."),
    ("📝", "Speech-to-Text", "Transcribe the uploaded audio."),
    ("🧠", "Semantic Similarity", "Compare the explanation with a reference concept."),
    ("📊", "Score Generation", "View similarity-based analysis scores."),
    ("💬", "Feedback", "Receive feedback based on the analysis result."),
    ("📄", "PDF Report", "Download an analysis report."),
    ("📈", "Dashboard", "Review analysis history and summary charts."),
    ("💾", "SQLite Database", "Store analysis history locally."),
]

features_html = "".join(
    f"""
    <div class="feature-card">
        <div class="feature-icon">{icon}</div>
        <h3 class="feature-title">{title}</h3>
        <p class="feature-description">{description}</p>
    </div>
    """
    for icon, title, description in features
)
st.html(f'<div class="vbcua-grid vbcua-grid-4">{features_html}</div>')

st.divider()

# -------------------------------------------------------------------
# Technologies Used
# -------------------------------------------------------------------
st.header("🛠 Technologies Used")
technologies = [
    ("🐍", "Application", ["Python", "Streamlit"]),
    ("🤖", "AI Models", ["Faster Whisper", "Sentence-BERT"]),
    ("📚", "Supporting Libraries", ["SQLite", "ReportLab", "Librosa", "Matplotlib", "Plotly"]),
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
st.html(f'<div class="vbcua-grid vbcua-grid-3">{tech_html}</div>')

st.divider()

# -------------------------------------------------------------------
# System Workflow
# -------------------------------------------------------------------
st.header("⚙️ System Workflow")
workflow = [
    ("1", "Upload and Validate Audio"),
    ("2", "Generate Waveform and Transcribe Speech"),
    ("3", "Analyze Audio Statistics"),
    ("4", "Load Reference Concept"),
    ("5", "Calculate Semantic Similarity"),
    ("6", "Match Reference Keywords"),
    ("7", "Calculate Scores and Generate Feedback"),
    ("8", "Generate PDF Report"),
    ("9", "Save Results to Database"),
    ("10", "Review Dashboard Analytics"),
]

workflow_html = "".join(
    f"""
    <div class="workflow-card">
        <div class="workflow-header">
            <span class="workflow-badge">{str(number).zfill(2)}</span>
            <span class="workflow-title">{title}</span>
        </div>
    </div>
    """
    for number, title in workflow
)
st.html(f'<div class="vbcua-grid vbcua-grid-workflow">{workflow_html}</div>')

st.divider()

# -------------------------------------------------------------------
# Future Scope
# -------------------------------------------------------------------
st.header("🚀 Future Scope")
st.caption("Planned enhancements; these are not currently implemented features.")

future_scope = [
    ("🎤", "Live voice recording"),
    ("🌐", "Multi-language support"),
    ("🤖", "AI chatbot tutor"),
    ("☁️", "Cloud deployment"),
    ("🔐", "Student login system"),
    ("👨‍🏫", "Teacher dashboard"),
    ("📈", "Performance prediction"),
]

future_html = "".join(
    f"""
    <div class="vbcua-card" style="padding: 0.9rem 1.1rem; min-height: 70px;">
        <div style="display: flex; align-items: center; gap: 0.65rem;">
            <span style="font-size: 1.25rem;">{icon}</span>
            <span style="color: var(--vbcua-navy); font-weight: 600; font-size: 0.95rem;">{enhancement}</span>
        </div>
    </div>
    """
    for icon, enhancement in future_scope
)
st.html(f'<div class="vbcua-grid vbcua-grid-workflow">{future_html}</div>')

st.divider()
st.info("Developed as an AI-based educational project using Machine Learning and Natural Language Processing.")