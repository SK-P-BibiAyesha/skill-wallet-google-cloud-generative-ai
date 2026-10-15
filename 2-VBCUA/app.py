from pathlib import Path
import streamlit as st

from database.database import create_table
from utils.helper import load_css

# Initialize database tables
create_table()

st.set_page_config(
    page_title="SkillWallet | Voice Concept Analyser",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply global styling
load_css()

# Sidebar Brand Header
with st.sidebar:
    st.markdown("""
    <div style="padding: 10px 4px 18px 4px; border-bottom: 1px solid rgba(255,255,255,0.08); margin-bottom: 14px;">
        <div style="display:flex; align-items:center; gap:12px;">
            <div style="width:42px; height:42px; border-radius:12px; background:linear-gradient(135deg, #6366F1 0%, #8B5CF6 100%); display:flex; align-items:center; justify-content:center; font-size:22px; box-shadow:0 4px 14px rgba(99,102,241,0.45); flex-shrink:0;">
                🎙️
            </div>
            <div>
                <div style="font-weight:800; font-size:17px; color:#F8FAFC; letter-spacing:-0.02em; line-height:1.2;">SkillWallet AI</div>
                <div style="font-size:12px; color:#818CF8; font-weight:500;">VBCUA Assessment Engine</div>
            </div>
        </div>
        <div style="margin-top:14px; display:inline-flex; align-items:center; gap:7px; background:rgba(16,185,129,0.12); border:1px solid rgba(16,185,129,0.3); border-radius:20px; padding:4px 12px; font-size:11px; color:#34D399; font-weight:600;">
            <span style="width:7px; height:7px; border-radius:50%; background:#10B981; display:inline-block; box-shadow:0 0 8px #10B981;"></span>
            Whisper & S-BERT Active
        </div>
    </div>
    """, unsafe_allow_html=True)

# Define application pages
home = st.Page(
    "pages/Home.py",
    title="Home Overview",
    icon="🏠",
    default=True
)

analyze = st.Page(
    "pages/Analyze_Audio.py",
    title="Analyze Voice",
    icon="🎙️"
)

dashboard = st.Page(
    "pages/Dashboard.py",
    title="Performance Dashboard",
    icon="📊"
)

reports = st.Page(
    "pages/Reports.py",
    title="Assessment Reports",
    icon="📋"
)

about = st.Page(
    "pages/About.py",
    title="System Architecture",
    icon="ℹ️"
)

navigation = st.navigation(
    {
        "Overview": [home, about],
        "Assessment Studio": [analyze, dashboard, reports],
    }
)

navigation.run()