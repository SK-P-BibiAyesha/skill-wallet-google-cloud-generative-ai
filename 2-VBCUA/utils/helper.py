from pathlib import Path
import streamlit as st


def load_css() -> None:
    """Load the VBCUA stylesheet using a path independent of the terminal cwd."""
    project_root = Path(__file__).resolve().parent.parent
    css_path = project_root / "assets" / "styles" / "custom.css"

    if not css_path.is_file():
        st.warning(f"Custom stylesheet was not found: {css_path}")
        return

    css = css_path.read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def create_feature_card(icon: str, title: str, description: str) -> None:
    """Render a reusable feature card."""
    st.markdown(
        f"""
        <div class="feature-card">
            <div class="feature-icon">{icon}</div>
            <h3 class="feature-title">{title}</h3>
            <p class="feature-description">{description}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
