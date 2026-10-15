from pathlib import Path
import streamlit as st


def load_css():
    """
    Load custom CSS styles reliably from any working directory.
    """
    base_dir = Path(__file__).resolve().parent.parent
    css_path = base_dir / "assets" / "styles" / "custom.css"
    if css_path.exists():
        with open(css_path, encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True,
            )


def create_feature_card(icon, title, description):
    """
    Display a reusable feature card.
    """
    st.markdown(
        f"""
        <div class="feature-card">
            <div class="feature-icon">{icon}</div>
            <div class="feature-title">{title}</div>
            <div class="feature-description">
                {description}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )