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
        "link": "https://dl.acm.org/doi/10.1145/3675249.3675335",
    },
    {
        "title": "Fault Diagnosis of Aero-engine Inter-shaft Bearings Using a Parallel SE-Depthwise Separable Convolutional Neural Network and Transformer Model",
        "conference": "IEEE 7th MCTE 2024 (Conference Paper, Accepted for Publication)",
    },
    {
        "title": "LawLuo: A Multi-Agent Collaborative Framework for Chinese Legal Consultation",
        "conference": "arXiv (Conference Paper/CCF-A, Under Review)",
        "link": "https://arxiv.org/abs/2407.16252",
    },
    {
        "title": "Study on breast cancer image detection and classification based on residual connected convolutional neural network (CNN)",
        "conference": "2nd International Conference on Modern Medicine and Global Health (Conference Paper, Published)",
        "link": "https://www.ewadirect.com/proceedings/tns/article/view/10586",
    },
    {
        "title": "Multimodal Large Language Model Enhancement Network for Multimodal Sentiment Analysis",
        "conference": "Journal Paper (JCR-Q1, Under Review)",
    },
    {
        "title": "Multi-Stage Simulation of Residents' Perception and Decision Making Behavior Regarding Disaster Risk Information: An Exploratory Study on Large Language Model Agents Driven Social-Cognitive Simulation Framework",
        "conference": "Journal Paper (JCR-Q1, Under Minor Revision)",
    },
    {
        "title": "Swin Transformer with Large Margin Aware Focal Loss for Automatic Classification of Diabetic Retinopathy",
        "conference": "Journal Paper (Scopus-Q3, Under Major Revision)",
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
