import streamlit as st
import pandas as pd

from database.queries import get_all_reports

from utils.helper import load_css

load_css()

st.set_page_config(
    page_title="Reports",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Analysis Reports")
st.markdown("Browse, search, and export all previous concept understanding analyses.")

st.divider()

reports = get_all_reports()

if not reports:
    st.info("No reports available.")
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

# ------------------------------------------------
# Summary Cards
# ------------------------------------------------

c1, c2, c3 = st.columns(3)

c1.metric("📄 Total Reports", len(df))
c2.metric("⭐ Average Score", f"{df['Overall Score'].mean():.2f}%")
c3.metric("🏆 Best Score", f"{df['Overall Score'].max():.2f}%")

st.divider()

# ------------------------------------------------
# Search
# ------------------------------------------------

search = st.text_input("🔍 Search Topic")

if search:
    df = df[df["Topic"].str.contains(search, case=False)]

# ------------------------------------------------
# Filter
# ------------------------------------------------

levels = ["All"] + sorted(df["Level"].unique().tolist())

selected_level = st.selectbox(
    "🎯 Filter by Understanding Level",
    levels
)

if selected_level != "All":
    df = df[df["Level"] == selected_level]

# ------------------------------------------------
# Sort
# ------------------------------------------------

sort_option = st.selectbox(
    "📅 Sort By",
    [
        "Newest First",
        "Oldest First",
        "Highest Score",
        "Lowest Score",
    ]
)

if sort_option == "Newest First":
    df = df.sort_values("Created At", ascending=False)

elif sort_option == "Oldest First":
    df = df.sort_values("Created At")

elif sort_option == "Highest Score":
    df = df.sort_values("Overall Score", ascending=False)

else:
    df = df.sort_values("Overall Score")

st.divider()

# ------------------------------------------------
# Report Table
# ------------------------------------------------

display_df = df[
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

# ------------------------------------------------
# Report Details
# ------------------------------------------------

st.divider()

st.subheader("📋 Detailed Reports")

for _, row in df.iterrows():

    with st.expander(
        f"{row['Topic']} | {row['Created At']}"
    ):

        st.write("### 📝 Transcript")
        st.write(row["Transcript"])

        st.write("### 📊 Scores")

        st.write(f"Similarity : {row['Similarity']:.2f}%")
        st.write(f"Overall : {row['Overall Score']:.2f}%")
        st.write(f"Concept Accuracy : {row['Concept Accuracy']:.2f}%")
        st.write(f"Explanation Quality : {row['Explanation Quality']:.2f}%")

        st.write("### 🎯 Understanding Level")
        st.success(row["Level"])

        st.write("### 💬 Feedback")
        st.write(row["Feedback"])

# ------------------------------------------------
# CSV Export
# ------------------------------------------------

st.divider()

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Export Reports as CSV",
    data=csv,
    file_name="analysis_reports.csv",
    mime="text/csv",
    width="stretch"
)