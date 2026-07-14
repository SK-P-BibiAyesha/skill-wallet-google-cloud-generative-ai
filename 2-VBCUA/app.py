import streamlit as st

from database.database import create_table

create_table()

st.set_page_config(
    page_title="Voice-Based Concept Understanding Analyser",
    page_icon="🎤",
    layout="wide"
)

home = st.Page(
    "pages/Home.py",
    title="Home",
    icon="🏠"
)

about = st.Page(
    "pages/About.py",
    title="About",
    icon="ℹ️"
)

analyze = st.Page(
    "pages/Analyze_Audio.py",
    title="Analyze Audio",
    icon="🎤"
)

dashboard = st.Page(
    "pages/Dashboard.py",
    title="Dashboard",
    icon="📊"
)

reports = st.Page(
    "pages/Reports.py",
    title="Reports",
    icon="📄"
)

navigation = st.navigation(
    [
        home,
        about,
        analyze,
        dashboard,
        reports,
    ]
)

navigation.run()