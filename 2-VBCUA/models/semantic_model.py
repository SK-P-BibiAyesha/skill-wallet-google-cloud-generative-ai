from sentence_transformers import SentenceTransformer, util
import streamlit as st

# Load Sentence-BERT only once
@st.cache_resource
def load_semantic_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


def calculate_similarity(reference_text, student_text):
    """
    Returns similarity score (0-100)
    """

    model = load_semantic_model()

    reference_embedding = model.encode(reference_text, convert_to_tensor=True)
    student_embedding = model.encode(student_text, convert_to_tensor=True)

    similarity = util.cos_sim(reference_embedding, student_embedding)

    score = float(similarity[0][0]) * 100

    if score < 0:
        score = 0

    if score > 100:
        score = 100

    return round(score, 2)