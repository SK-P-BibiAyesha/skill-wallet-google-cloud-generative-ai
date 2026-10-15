import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from database.queries import get_all_reports
from utils.helper import load_css

load_css()

# ======================================================
# Header
# ======================================================

st.markdown("""
<div style="margin-bottom: 24px;">
    <div style="display:inline-flex; align-items:center; gap:8px; padding:4px 14px; border-radius:9999px; background:rgba(99,102,241,0.12); border:1px solid rgba(99,102,241,0.25); color:#818CF8; font-size:12px; font-weight:600; text-transform:uppercase; letter-spacing:0.06em; margin-bottom:10px;">
        Assessment Intelligence
    </div>
    <h1 style="font-size:32px; font-weight:800; margin-bottom:6px;">📊 Analytics & Performance Dashboard</h1>
    <p style="color:#94A3B8; font-size:16px; margin:0;">
        Aggregated metrics, semantic trends, and cohort understanding distribution across all evaluation sessions.
    </p>
</div>
""", unsafe_allow_html=True)

reports = get_all_reports()

if not reports:
    st.info("📂 No assessment reports found in database. Complete an audio analysis to generate data.")
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

# Dark Plotly Layout Helper
def apply_dark_layout(fig):
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Plus Jakarta Sans, sans-serif", color="#94A3B8", size=12),
        margin=dict(l=20, r=20, t=40, b=20),
        legend=dict(
            font=dict(color="#CBD5E1"),
            bgcolor="rgba(17,24,39,0.6)",
            bordercolor="rgba(255,255,255,0.08)"
        )
    )
    fig.update_xaxes(
        gridcolor="rgba(255,255,255,0.06)",
        zerolinecolor="rgba(255,255,255,0.1)",
        tickfont=dict(color="#94A3B8")
    )
    fig.update_yaxes(
        gridcolor="rgba(255,255,255,0.06)",
        zerolinecolor="rgba(255,255,255,0.1)",
        tickfont=dict(color="#94A3B8")
    )
    return fig

# ======================================================
# Filters (Sidebar)
# ======================================================

st.sidebar.markdown("""
<div style="font-weight:700; font-size:15px; color:#F8FAFC; margin-bottom:12px; display:flex; align-items:center; gap:8px;">
    <span>🔍</span> Dashboard Filters
</div>
""", unsafe_allow_html=True)

selected_topic = st.sidebar.selectbox(
    "Filter by Topic",
    ["All"] + sorted(df["Topic"].unique().tolist())
)

selected_level = st.sidebar.selectbox(
    "Filter by Level",
    ["All"] + sorted(df["Level"].unique().tolist())
)

if selected_topic != "All":
    df = df[df["Topic"] == selected_topic]

if selected_level != "All":
    df = df[df["Level"] == selected_level]

if df.empty:
    st.warning("⚠️ No records match the selected filter criteria.")
    st.stop()

# ======================================================
# Top KPI Metric Cards
# ======================================================

total_reports = len(df)
average_score = df["Overall Score"].mean()
highest_score = df["Overall Score"].max()
lowest_score = df["Overall Score"].min()

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(label="📄 Total Assessments", value=total_reports)

with c2:
    st.metric(label="⭐ Cohort Mean Score", value=f"{average_score:.1f}%")

with c3:
    st.metric(label="🏆 Benchmark Peak", value=f"{highest_score:.1f}%")

with c4:
    st.metric(label="📉 Foundation Score", value=f"{lowest_score:.1f}%")

st.markdown("<hr>", unsafe_allow_html=True)

# ======================================================
# Charts Row 1: Overall Performance & Radar Analysis
# ======================================================

col_row1_left, col_row1_right = st.columns([1, 1], gap="medium")

with col_row1_left:
    st.markdown("#### 🎯 Overall Score Mastery")
    st.caption("Proportion of average score achieved out of total possible score")

    fig_gauge = px.pie(
        values=[average_score, max(0.1, 100 - average_score)],
        names=["Average Score", "Remaining"],
        hole=0.72,
        color_discrete_sequence=["#6366F1", "rgba(255, 255, 255, 0.08)"]
    )
    fig_gauge.update_traces(textinfo="none", hoverinfo="label+value")
    fig_gauge.update_layout(
        showlegend=False,
        annotations=[
            dict(
                text=f"<b>{average_score:.1f}%</b><br><span style='font-size:12px; color:#94A3B8;'>Average</span>",
                x=0.5,
                y=0.5,
                font_size=24,
                font_color="#F8FAFC",
                showarrow=False
            )
        ]
    )
    apply_dark_layout(fig_gauge)
    st.plotly_chart(fig_gauge, use_container_width=True)

with col_row1_right:
    st.markdown("#### 🕸 Performance Radar Map")
    st.caption("Multi-dimensional assessment across accuracy, quality, and semantic similarity")

    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=[
            average_score,
            df["Concept Accuracy"].mean(),
            df["Explanation Quality"].mean(),
            df["Similarity"].mean()
        ],
        theta=["Overall", "Concept", "Quality", "Similarity"],
        fill="toself",
        fillcolor="rgba(99, 102, 241, 0.25)",
        line=dict(color="#818CF8", width=2),
        name="Cohort Avg"
    ))
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                color="#64748B",
                gridcolor="rgba(255, 255, 255, 0.08)"
            ),
            angularaxis=dict(
                color="#CBD5E1",
                gridcolor="rgba(255, 255, 255, 0.08)"
            ),
            bgcolor="rgba(0,0,0,0)"
        ),
        showlegend=False
    )
    apply_dark_layout(fig_radar)
    st.plotly_chart(fig_radar, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ======================================================
# Charts Row 2: Topic Performance & Timeline Trend
# ======================================================

col_row2_left, col_row2_right = st.columns([1, 1], gap="medium")

with col_row2_left:
    st.markdown("#### 📚 Average Performance by Topic")

    topic_scores = df.groupby("Topic")["Overall Score"].mean().reset_index()
    best_topic = topic_scores.sort_values("Overall Score", ascending=False).iloc[0]["Topic"]

    st.markdown(f"""
    <div style="background:rgba(16,185,129,0.12); border:1px solid rgba(16,185,129,0.3); border-radius:12px; padding:10px 16px; margin-bottom:12px; font-size:13px; color:#34D399; font-weight:600;">
        🏆 Peak Performing Topic: <strong>{best_topic}</strong>
    </div>
    """, unsafe_allow_html=True)

    fig_bar = px.bar(
        topic_scores,
        x="Topic",
        y="Overall Score",
        color="Overall Score",
        color_continuous_scale=["#6366F1", "#8B5CF6", "#06B6D4"],
        text_auto=".1f"
    )
    fig_bar.update_layout(xaxis_title="", yaxis_title="Score (%)", coloraxis_showscale=False)
    apply_dark_layout(fig_bar)
    st.plotly_chart(fig_bar, use_container_width=True)

with col_row2_right:
    st.markdown("#### 📈 Historical Assessment Progression")
    st.caption("Chronological progression of evaluation scores over time")

    trend = df.sort_values("Created At")
    fig_trend = px.line(
        trend,
        x="Created At",
        y="Overall Score",
        markers=True
    )
    fig_trend.update_traces(
        line=dict(color="#06B6D4", width=3),
        marker=dict(size=8, color="#818CF8", line=dict(width=2, color="#FFFFFF"))
    )
    fig_trend.update_layout(xaxis_title="", yaxis_title="Overall Score (%)")
    apply_dark_layout(fig_trend)
    st.plotly_chart(fig_trend, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ======================================================
# Charts Row 3: Understanding Level & Concept Correlation
# ======================================================

col_row3_left, col_row3_right = st.columns([1, 1], gap="medium")

with col_row3_left:
    st.markdown("#### 🎯 Understanding Level Distribution")
    level_counts = df["Level"].value_counts().reset_index()
    level_counts.columns = ["Level", "Count"]

    fig_levels = px.pie(
        level_counts,
        names="Level",
        values="Count",
        hole=0.55,
        color_discrete_sequence=["#10B981", "#6366F1", "#F59E0B", "#EF4444"]
    )
    fig_levels.update_traces(textposition="inside", textinfo="percent+label")
    apply_dark_layout(fig_levels)
    st.plotly_chart(fig_levels, use_container_width=True)

with col_row3_right:
    st.markdown("#### 🔬 Concept Accuracy vs Explanation Quality")
    fig_scatter = px.scatter(
        df,
        x="Concept Accuracy",
        y="Explanation Quality",
        color="Overall Score",
        size="Overall Score",
        hover_data=["Topic", "Level"],
        color_continuous_scale=["#6366F1", "#A855F7", "#EC4899"]
    )
    apply_dark_layout(fig_scatter)
    st.plotly_chart(fig_scatter, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ======================================================
# Recent Reports Table
# ======================================================

st.markdown("#### 📋 Recent Assessment Records")
display_df = df[
    [
        "Topic",
        "Similarity",
        "Overall Score",
        "Concept Accuracy",
        "Explanation Quality",
        "Level",
        "Created At"
    ]
].sort_values("Created At", ascending=False)

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)