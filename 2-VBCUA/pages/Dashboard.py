import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from database.queries import get_all_reports

from utils.helper import load_css


def style_chart(figure):
    figure.update_layout(
        template="plotly_white",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        plot_bgcolor="rgba(0, 0, 0, 0)",
        font=dict(family="Arial, sans-serif", size=12, color="#1c2c42"),
        margin=dict(l=24, r=24, t=54, b=28),
    )
    figure.update_xaxes(gridcolor="#e7edf3", zerolinecolor="#dce5ee")
    figure.update_yaxes(gridcolor="#e7edf3", zerolinecolor="#dce5ee")
    return figure


load_css()

st.title("📊 Analytics Dashboard")
st.caption("A summary of saved concept-understanding analyses.")

st.divider()

reports = get_all_reports()

if not reports:
    total_column, average_column, highest_column, lowest_column = st.columns(4)
    total_column.metric("📄 Total Reports", 0)
    average_column.metric("⭐ Average Score", "—")
    highest_column.metric("🏆 Highest Score", "—")
    lowest_column.metric("📉 Lowest Score", "—")
    st.info("No reports yet. Upload an audio explanation to start a new analysis.")
    if st.button(
        "🎤 Analyze Audio",
        type="primary",
        width="content",
        key="analyze-from-empty-dashboard",
    ):
        st.switch_page("pages/Analyze_Audio.py")
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


# -------------------------
# Filters
# -------------------------

st.sidebar.header("🔍 Filters")

selected_topic = st.sidebar.selectbox(
    "Topic",
    ["All"] + sorted(df["Topic"].unique().tolist())
)

selected_level = st.sidebar.selectbox(
    "Understanding Level",
    ["All"] + sorted(df["Level"].unique().tolist())
)

if selected_topic != "All":
    df = df[df["Topic"] == selected_topic]

if selected_level != "All":
    df = df[df["Level"] == selected_level]

total_saved_reports = len(reports)
st.caption(
    f"Showing {len(df)} reports matching the active filters "
    f"out of {total_saved_reports} saved reports."
)

if df.empty:
    total_column, average_column, highest_column, lowest_column = st.columns(4)
    total_column.metric("📄 Total Saved Reports", total_saved_reports)
    average_column.metric("⭐ Average Score", "—")
    highest_column.metric("🏆 Highest Score", "—")
    lowest_column.metric("📉 Lowest Score", "—")
    st.info("No reports match the selected filters.")
    st.stop()

# -------------------------
# Summary Cards
# -------------------------

total_reports = len(df)
average_score = df["Overall Score"].mean()
highest_score = df["Overall Score"].max()
lowest_score = df["Overall Score"].min()

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    label="📄 Reports in View",
    value=total_reports
)

c2.metric(
    label="⭐ Average Score",
    value=f"{average_score:.2f}%"
)

c3.metric(
    label="🏆 Highest Score",
    value=f"{highest_score:.2f}%"
)

c4.metric(
    label="📉 Lowest Score",
    value=f"{lowest_score:.2f}%"
)

topic_scores = (
    df.groupby("Topic")["Overall Score"]
    .mean()
    .reset_index()
)


best_topic = (
    topic_scores.sort_values(
        "Overall Score",
        ascending=False
    )
    .iloc[0]["Topic"]
)

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("🎯 Overall Performance")
    fig = px.pie(
        values=[average_score, 100 - average_score],
        names=["Average Score", "Remaining"],
        hole=0.76,
        color_discrete_sequence=["#0f766e", "#dce5ef"],
    )
    fig.update_traces(textinfo="none", sort=False)
    fig.update_layout(
        showlegend=False,
        annotations=[
            dict(
                text=f"{average_score:.1f}%",
                x=0.5,
                y=0.5,
                font=dict(size=26, color="#142238"),
                showarrow=False,
            )
        ],
    )
    st.plotly_chart(style_chart(fig), width="stretch")

with right:
    st.subheader("🕸 Performance Radar")
    radar = go.Figure()
    radar.add_trace(
        go.Scatterpolar(
            r=[
                average_score,
                df["Concept Accuracy"].mean(),
                df["Explanation Quality"].mean(),
                df["Similarity"].mean(),
            ],
            theta=["Overall", "Concept", "Quality", "Similarity"],
            fill="toself",
            fillcolor="rgba(15, 118, 110, .16)",
            line=dict(color="#0f766e", width=2),
            name="Performance",
        )
    )
    radar.update_layout(
        polar=dict(
            bgcolor="rgba(0, 0, 0, 0)",
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                gridcolor="#e7edf3",
                linecolor="#dce5ee",
            ),
        ),
        showlegend=False,
    )
    st.plotly_chart(style_chart(radar), width="stretch")

# -------------------------
# Topic scores and score trend
# -------------------------

left, right = st.columns(2)

with left:
    st.subheader("📚 Average Score by Topic")
    st.success(f"🏆 Best Performing Topic: **{best_topic}**")
    fig1 = px.bar(
        topic_scores,
        x="Topic",
        y="Overall Score",
        color="Overall Score",
        text_auto=".2f",
        color_continuous_scale=["#ccfbf1", "#0f766e"],
    )
    fig1.update_layout(xaxis_title="Topic", yaxis_title="Average Score")
    st.plotly_chart(style_chart(fig1), width="stretch")

with right:
    st.subheader("📈 Overall Score Trend")
    trend = df.sort_values("Created At")
    fig2 = px.line(
        trend,
        x="Created At",
        y="Overall Score",
        markers=True,
    )
    fig2.update_traces(
        line_width=3,
        marker_size=8,
        line_color="#0f766e",
        marker_color="#0f766e",
    )
    st.plotly_chart(style_chart(fig2), width="stretch")

# -------------------------
# Understanding levels and similarity distribution
# -------------------------

left, right = st.columns(2)

with left:
    st.subheader("🎯 Understanding Levels")
    level_counts = df["Level"].value_counts().reset_index()
    level_counts.columns = ["Level", "Count"]
    fig3 = px.pie(
        level_counts,
        names="Level",
        values="Count",
        hole=0.55,
        color_discrete_sequence=["#0f766e", "#1e3a5f", "#76aeb2", "#b45309"],
    )
    fig3.update_traces(textposition="inside", textinfo="percent+label")
    st.plotly_chart(style_chart(fig3), width="stretch")

with right:
    st.subheader("📊 Similarity Distribution")
    fig4 = px.histogram(
        df,
        x="Similarity",
        nbins=20,
        marginal="box",
        color_discrete_sequence=["#0f766e"],
    )
    st.plotly_chart(style_chart(fig4), width="stretch")

st.divider()

st.subheader("📈 Concept Accuracy vs Quality")
fig5 = px.scatter(
    df,
    x="Concept Accuracy",
    y="Explanation Quality",
    color="Overall Score",
    size="Overall Score",
    hover_data=["Topic", "Level"],
    color_continuous_scale=["#ccfbf1", "#0f766e"],
)
st.plotly_chart(style_chart(fig5), width="stretch")

st.subheader("📋 Recent Analysis Reports")
display = df[
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
styled_df = (
    display.sort_values("Created At", ascending=False)
    .style.background_gradient(subset=["Overall Score"], cmap="GnBu")
)
st.dataframe(styled_df, width="stretch", hide_index=True)