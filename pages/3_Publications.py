import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Daicx668",
    page_icon="🚀",
    layout="wide",
)

st.title("Publications📖")
st.divider()

# Define publications
publications = [
    {
        "title": "From the Perspective of Explainable Machine Learning: A Student Feature Selection Strategy Based on the Geometric Mean of Feature Importance and Robustness",
        "conference": "ACM ICCMT 2024 (Conference Paper, Published)",
        "link": "YOUR_LINK_TO_PAPER",
    },
    {
        "title": "Fault Diagnosis of Aero-engine Inter-shaft Bearings Using a Parallel SE-Depthwise Separable Convolutional Neural Network and Transformer Model",
        "conference": "IEEE 7th MCTE 2024 (Conference Paper, Accepted for Publication)",
    },
    {
        "title": "LawLuo: A Multi-Agent Collaborative Framework for Chinese Legal Consultation",
        "conference": "arXiv (Conference Paper/CCF-A, Under Review)",
        "link": "YOUR_LINK_TO_PAPER",
    },
    {
        "title": "Multimodal Large Language Model Enhancement Network for Multimodal Sentiment Analysis",
        "conference": "Journal Paper (JCR-Q1, Under Review)",
    },
    {
        "title": "Multi-Stage Simulation of Residents' Perception and Decision Making Behavior Regarding Disaster Risk Information: An Exploratory Study on Large Language Model Agents Driven Social-Cognitive Simulation Framework",
        "conference": "Journal Paper (JCR-Q1, Minor Revision)",
    },
    {
        "title": "Swin Transformer with Large Margin Aware Focal Loss for Automatic Classification of Diabetic Retinopathy",
        "conference": "Journal Paper (Scopus-Q3, Major Revision)",
    },
]

# Display publications
for pub in publications:
    st.markdown(
        f"""
        ### {pub['title']}
        **Conference/Journal:** {pub['conference']}
        {"[Read Full Text](" + pub['link'] + ")" if 'link' in pub else ""}
        """
    )
    st.markdown("---")
