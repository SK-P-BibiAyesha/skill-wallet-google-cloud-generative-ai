import streamlit as st
from utils.helper import load_css

load_css()

st.title("ℹ️ About VBCUA")
st.caption("A voice-based educational assessment platform.")

with st.container(border=True, key="about-intro"):
    st.subheader("🎤 Voice-Based Concept Understanding Analyser")
    st.write(
        "The Voice-Based Concept Understanding Analyser (VBCUA) evaluates a "
        "student's conceptual understanding through spoken explanations. "
        "Instead of checking only for exact words, it compares the explanation's "
        "semantic meaning with a reference concept."
    )

st.divider()

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
for index in range(0, len(features), 2):
    columns = st.columns(2)
    for feature_index, (column, (icon, title, description)) in enumerate(
        zip(columns, features[index:index + 2]),
        start=index,
    ):
        with column:
            with st.container(border=True, key=f"about-feature-{feature_index}"):
                st.markdown(f"### {icon} {title}")
                st.write(description)

st.divider()

st.header("🛠 Technologies Used")
technologies = [
    ("🐍", "Application", ["Python", "Streamlit"]),
    ("🤖", "AI Models", ["Faster Whisper", "Sentence-BERT"]),
    ("📚", "Supporting Libraries", ["SQLite", "ReportLab", "Librosa", "Matplotlib", "Plotly"]),
]
columns = st.columns(3)
for technology_index, (column, (icon, title, items)) in enumerate(
    zip(columns, technologies)
):
    with column:
        with st.container(border=True, key=f"about-technology-{technology_index}"):
            st.markdown(f"### {icon} {title}")
            st.markdown("\n".join(f"- {item}" for item in items))

st.divider()

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
for index in range(0, len(workflow), 3):
    columns = st.columns(3)
    for step_index, (column, (number, title)) in enumerate(
        zip(columns, workflow[index:index + 3]),
        start=index,
    ):
        with column:
            with st.container(border=True, key=f"about-step-{step_index}"):
                st.markdown(f"### {number}. {title}")

st.divider()

st.header("🚀 Future Scope")
st.caption("Planned enhancements; these are not currently implemented features.")
future_scope = [
    "Live voice recording",
    "Multi-language support",
    "AI chatbot tutor",
    "Cloud deployment",
    "Student login system",
    "Teacher dashboard",
    "Performance prediction",
]
columns = st.columns(2)
for index, enhancement in enumerate(future_scope):
    with columns[index % 2]:
        with st.container(border=True, key=f"about-future-{index}"):
            st.write(f"→ {enhancement}")

st.divider()

st.info("Developed as an AI-based educational project using Machine Learning and Natural Language Processing.")