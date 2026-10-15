import streamlit as st
import pandas as pd

from database.queries import get_all_reports
from utils.helper import load_css

load_css()

# ======================================================
# Header
# ======================================================

st.markdown("""
<div style="margin-bottom: 24px;">
    <div style="display:inline-flex; align-items:center; gap:8px; padding:4px 14px; border-radius:9999px; background:rgba(99,102,241,0.12); border:1px solid rgba(99,102,241,0.25); color:#818CF8; font-size:12px; font-weight:600; text-transform:uppercase; letter-spacing:0.06em; margin-bottom:10px;">
        Assessment Archives
    </div>
    <h1 style="font-size:32px; font-weight:800; margin-bottom:6px;">📋 Assessment History & Reports</h1>
    <p style="color:#94A3B8; font-size:16px; margin:0;">
        Search, filter, audit, and export verified oral evaluation reports.
    </p>
</div>
""", unsafe_allow_html=True)

reports = get_all_reports()

if not reports:
    st.info("📂 No assessment reports recorded yet. Perform an evaluation in the Assessment Studio to get started.")
    st.stop()

df = pd.DataFrame(
    reports,
    columns=[
        "ID",
        "Topic",
        "Transcript",
        "Similarity",
        "Overall Score",
        "Concept Accuracy",
        "Explanation Quality",
        "Level",
        "Feedback",
        "Created At"
    ]
)

# ======================================================
# Summary KPI Row
# ======================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("📄 Total Submissions", len(df))

with c2:
    st.metric("⭐ Cohort Mean Score", f"{df['Overall Score'].mean():.1f}%")

with c3:
    st.metric("🏆 Peak Benchmark", f"{df['Overall Score'].max():.1f}%")

with c4:
    best_topic = df.groupby("Topic")["Overall Score"].mean().idxmax()
    st.metric("🥇 Top Domain", best_topic)

st.markdown("<hr>", unsafe_allow_html=True)

# ======================================================
# Filter Controls Bar
# ======================================================

st.markdown("#### 🔍 Filter & Sort Repository")

f_col1, f_col2, f_col3 = st.columns([1.5, 1, 1], gap="medium")

with f_col1:
    search = st.text_input("Search by Topic name", placeholder="Type e.g. Machine Learning, Cloud...")

with f_col2:
    levels = ["All Levels"] + sorted(df["Level"].unique().tolist())
    selected_level = st.selectbox("Understanding Level", levels)

with f_col3:
    sort_option = st.selectbox(
        "Sort Order",
        [
            "Newest First",
            "Oldest First",
            "Highest Score",
            "Lowest Score",
        ]
    )

# Apply filters
filtered_df = df.copy()

if search:
    filtered_df = filtered_df[filtered_df["Topic"].str.contains(search, case=False)]

if selected_level != "All Levels":
    filtered_df = filtered_df[filtered_df["Level"] == selected_level]

if sort_option == "Newest First":
    filtered_df = filtered_df.sort_values("Created At", ascending=False)
elif sort_option == "Oldest First":
    filtered_df = filtered_df.sort_values("Created At")
elif sort_option == "Highest Score":
    filtered_df = filtered_df.sort_values("Overall Score", ascending=False)
else:
    filtered_df = filtered_df.sort_values("Overall Score")

# ======================================================
# Main Data Table
# ======================================================

st.markdown(f"#### 📊 Records Overview ({len(filtered_df)} items found)")

display_df = filtered_df[
    [
        "Topic",
        "Similarity",
        "Overall Score",
        "Concept Accuracy",
        "Explanation Quality",
        "Level",
        "Created At",
    ]
]

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True,
)

st.markdown("<hr>", unsafe_allow_html=True)

# ======================================================
# Detailed Expandable Cards
# ======================================================

st.markdown("#### 📖 Detailed Assessment Transcripts & Feedback")

for _, row in filtered_df.iterrows():
    level_color = "#10B981" if "High" in str(row["Level"]) or "Mastery" in str(row["Level"]) or "Advanced" in str(row["Level"]) else ("#F59E0B" if "Moderate" in str(row["Level"]) or "Proficient" in str(row["Level"]) else "#EF4444")

    with st.expander(f"📌 {row['Topic']}  •  Score: {row['Overall Score']:.1f}%  •  {row['Created At']}"):
        exp_col1, exp_col2 = st.columns([1.4, 1], gap="medium")

        with exp_col1:
            st.markdown("##### 📝 Transcribed Speech")
            st.markdown(f"""
            <div style="background:rgba(17,24,39,0.7); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:16px; font-size:14px; color:#CBD5E1; line-height:1.7;">
                {row['Transcript']}
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)
            st.markdown("##### 🤖 AI Feedback & Analysis")
            st.markdown(f"""
            <div style="background:rgba(99,102,241,0.08); border:1px solid rgba(99,102,241,0.25); border-radius:12px; padding:14px; font-size:13px; color:#E2E8F0; line-height:1.6;">
                {row['Feedback']}
            </div>
            """, unsafe_allow_html=True)

        with exp_col2:
            st.markdown("##### 📊 Metric Breakdown")
            st.markdown(f"""
            <div style="background:#111726; border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:16px;">
                <div style="margin-bottom:12px; display:flex; justify-content:space-between;">
                    <span style="color:#94A3B8; font-size:13px;">Overall Score</span>
                    <strong style="color:#818CF8;">{row['Overall Score']:.1f}%</strong>
                </div>
                <div style="margin-bottom:12px; display:flex; justify-content:space-between;">
                    <span style="color:#94A3B8; font-size:13px;">Semantic Similarity</span>
                    <strong style="color:#38BDF8;">{row['Similarity']:.1f}%</strong>
                </div>
                <div style="margin-bottom:12px; display:flex; justify-content:space-between;">
                    <span style="color:#94A3B8; font-size:13px;">Concept Accuracy</span>
                    <strong style="color:#34D399;">{row['Concept Accuracy']:.1f}%</strong>
                </div>
                <div style="margin-bottom:14px; display:flex; justify-content:space-between;">
                    <span style="color:#94A3B8; font-size:13px;">Explanation Quality</span>
                    <strong style="color:#A78BFA;">{row['Explanation Quality']:.1f}%</strong>
                </div>
                <div style="padding-top:10px; border-top:1px solid rgba(255,255,255,0.08); display:flex; justify-content:space-between; align-items:center;">
                    <span style="color:#94A3B8; font-size:12px;">Level</span>
                    <span style="background:rgba(255,255,255,0.05); color:{level_color}; font-weight:700; padding:3px 10px; border-radius:6px; font-size:12px;">{row['Level']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ======================================================
# CSV Export
# ======================================================

st.markdown("#### 💾 Export Dataset")
csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Export Filtered Reports as CSV",
    data=csv_data,
    file_name="vbcua_assessment_reports.csv",
    mime="text/csv",
    use_container_width=True
)