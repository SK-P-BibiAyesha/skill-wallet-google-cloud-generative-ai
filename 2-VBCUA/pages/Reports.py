import datetime
import os
import sqlite3
from time import timezone
from zoneinfo import ZoneInfo

import pandas as pd
import streamlit as st

from database.queries import delete_all_reports, get_all_reports
from utils.helper import load_css


load_css()

st.title("📄 Analysis Reports")
st.caption("Browse, filter, export, and manage saved analysis history.")
st.divider()

if "confirm_history_reset" not in st.session_state:
    st.session_state.confirm_history_reset = False

if st.session_state.pop("history_reset_notice", None) is not None:
    st.success("Report history was cleared successfully.")

reports = get_all_reports()

if st.session_state.confirm_history_reset:
    with st.container(border=True, key="history-reset-confirmation"):
        st.warning(
            f"This permanently deletes all {len(reports)} saved analysis-history "
            "records from the local database. It does not delete audio files, "
            "generated PDF files, reference concepts, or other data."
        )
        confirm_column, cancel_column = st.columns(2)
        with confirm_column:
            confirm_delete = st.button(
                "Confirm Delete",
                type="primary",
                width="stretch",
                key="confirm-delete-history",
            )
        with cancel_column:
            cancel_delete = st.button(
                "Cancel",
                width="stretch",
                key="cancel-delete-history",
            )

        if cancel_delete:
            st.session_state.confirm_history_reset = False
            st.rerun()

        if confirm_delete:
            try:
                deleted_count = delete_all_reports()
            except sqlite3.Error as error:
                st.error(f"Could not clear report history: {error}")
            else:
                st.session_state.confirm_history_reset = False
                st.session_state.history_reset_notice = deleted_count
                for key in (
                    "report_topic_search",
                    "report_level_filter",
                    "report_sort_order",
                ):
                    st.session_state.pop(key, None)
                st.rerun()
else:
    if reports and st.button(
        "🗑️ Reset History",
        width="content",
        key="request-reset-history",
    ):
        st.session_state.confirm_history_reset = True
        st.rerun()

if st.session_state.confirm_history_reset:
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
        "Created At",
    ],
)


# Display stored UTC timestamps in Indian Standard Time.
india_timezone = ZoneInfo("Asia/Kolkata")


def format_created_at(value):
    if pd.isna(value):
        return value

    timestamp = datetime.fromisoformat(str(value))

    # SQLite CURRENT_TIMESTAMP values are UTC and have no timezone suffix.
    if timestamp.tzinfo is None:
        timestamp = timestamp.replace(tzinfo=timezone.utc)

    return timestamp.astimezone(india_timezone).strftime("%Y-%m-%d %H:%M:%S")


df["Created At"] = df["Created At"].apply(format_created_at)
overall_scores = pd.to_numeric(df["Overall Score"], errors="coerce").dropna()

total_column, average_column, best_column = st.columns(3)
total_column.metric("📄 Total Reports", len(df))
average_column.metric(
    "⭐ Average Score",
    f"{overall_scores.mean():.2f}%" if not overall_scores.empty else "—",
)
best_column.metric(
    "🏆 Best Score",
    f"{overall_scores.max():.2f}%" if not overall_scores.empty else "—",
)

if df.empty:
    st.info("No reports yet. Upload an audio explanation to start a new analysis.")
    if st.button(
        "🎤 Analyze Audio",
        type="primary",
        width="content",
        key="analyze-from-empty-reports",
    ):
        st.switch_page("pages/Analyze_Audio.py")
    st.stop()

st.divider()

search_column, level_column, sort_column = st.columns([2, 1, 1])
with search_column:
    search = st.text_input("🔍 Search Topic", key="report_topic_search")

levels = ["All"] + sorted(df["Level"].dropna().unique().tolist())
with level_column:
    selected_level = st.selectbox(
        "🎯 Understanding Level",
        levels,
        key="report_level_filter",
    )

with sort_column:
    sort_option = st.selectbox(
        "📅 Sort By",
        [
            "Newest First",
            "Oldest First",
            "Highest Score",
            "Lowest Score",
        ],
        key="report_sort_order",
    )

filtered_df = df
if search:
    filtered_df = filtered_df[
        filtered_df["Topic"].fillna("").str.contains(
            search,
            case=False,
            regex=False,
        )
    ]

if selected_level != "All":
    filtered_df = filtered_df[filtered_df["Level"] == selected_level]

sort_options = {
    "Newest First": ("Created At", False),
    "Oldest First": ("Created At", True),
    "Highest Score": ("Overall Score", False),
    "Lowest Score": ("Overall Score", True),
}
sort_column_name, ascending = sort_options[sort_option]
filtered_df = filtered_df.sort_values(sort_column_name, ascending=ascending)

st.caption(f"Showing {len(filtered_df)} of {len(df)} saved reports.")
if filtered_df.empty:
    st.info("No reports match these filters. Adjust the search or level filter.")
    st.stop()

st.divider()

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
    width="stretch",
    hide_index=True,
)

st.divider()
st.subheader("📋 Detailed Reports")

for _, row in filtered_df.iterrows():
    with st.expander(f"{row['Topic']} | {row['Created At']}"):
        st.write("### 📝 Transcript")
        st.write(row["Transcript"])

        st.write("### 📊 Scores")
        st.write(f"Similarity: {row['Similarity']:.2f}%")
        st.write(f"Overall: {row['Overall Score']:.2f}%")
        st.write(f"Concept Accuracy: {row['Concept Accuracy']:.2f}%")
        st.write(f"Explanation Quality: {row['Explanation Quality']:.2f}%")

        st.write("### 🎯 Understanding Level")
        st.success(row["Level"])

        st.write("### 💬 Feedback")
        st.write(row["Feedback"])

        pdf_path = f"reports/{row['Topic']}_Analysis_Report.pdf"
        if os.path.exists(pdf_path):
            with open(pdf_path, "rb") as pdf_file:
                st.download_button(
                    label=f"📥 Download {row['Topic']} PDF Report",
                    data=pdf_file.read(),
                    file_name=f"{row['Topic']}_Analysis_Report.pdf",
                    mime="application/pdf",
                    key=f"download-pdf-{row['ID']}",
                    width="stretch",
                )

st.divider()

csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="⬇ Export Reports as CSV",
    data=csv,
    file_name="analysis_reports.csv",
    mime="text/csv",
    width="stretch",
)
