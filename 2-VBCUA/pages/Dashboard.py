import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from database.queries import get_all_reports

from utils.helper import load_css

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)


load_css()


st.title("📊 Analytics Dashboard")
st.markdown("Overview of all concept understanding analyses.")

st.divider()

reports = get_all_reports()

if not reports:
    st.info("No analysis reports available.")
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

if df.empty:
    st.warning("No reports found for the selected filters.")
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
    label="📄 Total Reports",
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

st.divider()

st.subheader("🎯 Overall Performance")

fig = px.pie(
    values=[average_score, 100-average_score],
    names=["Average Score", ""],
    hole=0.75
)

fig.update_traces(
    textinfo="none"
)

fig.update_layout(
    showlegend=False,
    annotations=[
        dict(
            text=f"{average_score:.1f}%",
            x=0.5,
            y=0.5,
            font_size=28,
            showarrow=False
        )
    ]
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()



st.subheader("🕸 Performance Radar")

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=[
        average_score,
        df["Concept Accuracy"].mean(),
        df["Explanation Quality"].mean(),
        df["Similarity"].mean()
    ],
    theta=[
        "Overall",
        "Concept",
        "Quality",
        "Similarity"
    ],
    fill="toself",
    name="Performance"
))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100]
        )
    ),
    showlegend=False
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# -------------------------
# Topic Average Score
# -------------------------

st.subheader("📚 Average Score by Topic")



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

st.success(
    f"🏆 Best Performing Topic: **{best_topic}**"
)


fig1 = px.bar(
    topic_scores,
    x="Topic",
    y="Overall Score",
    color="Overall Score",
    text_auto=".2f",
    title="Average Score by Topic"
)

fig1.update_layout(
    xaxis_title="Topic",
    yaxis_title="Average Score",
)

st.plotly_chart(fig1, use_container_width=True)

# -------------------------
# Score Trend
# -------------------------

st.subheader("📈 Overall Score Trend")

trend = df.sort_values("Created At")

fig2 = px.line(
    trend,
    x="Created At",
    y="Overall Score",
    markers=True,
    title="Overall Score Trend"
)

fig2.update_traces(
    line_width=4,
    marker_size=10
)

st.plotly_chart(fig2, use_container_width=True)

# -------------------------
# Understanding Levels
# -------------------------

st.subheader("🎯 Understanding Levels")

level_counts = (
    df["Level"]
    .value_counts()
    .reset_index()
)

level_counts.columns = ["Level", "Count"]

fig3 = px.pie(
    level_counts,
    names="Level",
    values="Count",
    hole=0.55,
    title="Understanding Level Distribution"
)

fig3.update_traces(
    textposition="inside",
    textinfo="percent+label"
)

st.plotly_chart(fig3, use_container_width=True)

# -------------------------
# Similarity Distribution
# -------------------------

st.subheader("📊 Similarity Distribution")

fig4 = px.histogram(
    df,
    x="Similarity",
    nbins=20,
    marginal="box",
    title="Similarity Distribution"
)

st.plotly_chart(fig4, use_container_width=True)

st.divider()

st.subheader("📈 Concept Accuracy vs Quality")

fig5 = px.scatter(
    df,
    x="Concept Accuracy",
    y="Explanation Quality",
    color="Overall Score",
    size="Overall Score",
    hover_data=["Topic", "Level"],
    title="Concept Accuracy vs Explanation Quality"
)

st.plotly_chart(
    fig5,
    use_container_width=True
)


# -------------------------
# Recent Reports
# -------------------------

st.subheader("📋 Recent Analysis Reports")

display = df[
    [
        "Topic",
        "Similarity",
        "Overall Score",
        "Concept Accuracy",
        "Explanation Quality",
        "Level",
        "Created At"
    ]
]

styled_df = (
    display.sort_values(
        "Created At",
        ascending=False
    )
    .style.background_gradient(
        subset=["Overall Score"],
        cmap="Greens"
    )
)

st.dataframe(
    styled_df,
    use_container_width=True,
    hide_index=True
)