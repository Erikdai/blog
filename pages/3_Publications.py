import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Daicx668",
    page_icon="🚀",
    layout="wide",
)

st.title("📖 Publications")
st.divider()



# Define publications
publications = [
    {
        "title": "CLAUSE: Agentic Neuro-Symbolic Knowledge Graph Reasoning via Dynamic Learnable Context Engineering",
        "conference": "The 14th International Conference on Learning Representations (ICLR 2026)",
        "link": "https://arxiv.org/abs/2509.21035",
    },
    {
        "title": "From Metaphor to Mechanism: How LLMs Decode Traditional Chinese Medicine Symbolic Language for Modern Clinical Relevance",
        "conference": "IEEE 2025 International Joint Conference on Neural Networks (IJCNN 2025)",
        "link": "https://ieeexplore.ieee.org/document/11228098"
    },
    {
        "title": "Multimodal Large Language Model Enhancement Network for Multimodal Sentiment Analysis",
        "conference": "Springer Nature - Multimedia Systems",
        "link": "https://link.springer.com/article/10.1007/s00530-025-01914-2"
    },
    {
        "title": "Multi-Stage Simulation of Residents' Perception and Decision Making Behavior Regarding Disaster Risk Information: An Exploratory Study on Large Language Model Agents Driven Social-Cognitive Simulation Framework",
        "conference": "MDPI - Systems",
        "link": "https://www.mdpi.com/2079-8954/13/4/240"
    },
    {
        "title": "MEGA-RAG: a retrieval-augmented generation framework with multi-evidence guided answer refinement for mitigating hallucinations of LLMs in public health",
        "conference": "Frontiers in Public Health",
        "link": "https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2025.1635381/full",
    },
    {
        "title": "From the Perspective of Explainable Machine Learning: A Student Feature Selection Strategy Based on the Geometric Mean of Feature Importance and Robustness",
        "conference": "ACM The 2024 International Conference on Computer and Multimedia Technology",
        "link": "https://dl.acm.org/doi/10.1145/3675249.3675335",
    },
    {
        "title": "Fault Diagnosis of Aero-engine Inter-shaft Bearings Using a Parallel SE-Depthwise Separable Convolutional Neural Network and Transformer Model",
        "conference": "IEEE 2024 7th International Conference on Mechatronics and Computer Technology Engineering",
        "link": "https://ieeexplore.ieee.org/abstract/document/11117663"
    },
    {
        "title": "LawLuo: A Multi-Agent Collaborative Framework for Chinese Legal Consultation",
        "conference": "arXiv (Under Review)",
        "link": "https://arxiv.org/abs/2407.16252",
    },
]

# 展示 publications
for idx, pub in enumerate(publications, start=1):
    st.markdown(
        f"""
        <div style="background-color: #2c2f33; padding: 15px; border-radius: 10px; margin-bottom: 20px; color: #f1f1f1;">
            <h3 style="color: #4DB6AC;">{pub['title']}</h3>
            <p><b>Conference/Journal:</b> {pub['conference']}</p>
            {"<a href='" + pub['link'] + "' target='_blank' style='color: #64B5F6; text-decoration: none;'>Paper Link🔗</a>" if 'link' in pub else ""}
        </div>
        """,
        unsafe_allow_html=True,
    )
