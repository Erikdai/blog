import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Daicx668",
    page_icon="🚀",
    layout="wide",
)

st.title("📖 Publications")
st.divider()

# Define publications with images
publications = [
    {
        "title": "From the Perspective of Explainable Machine Learning: A Student Feature Selection Strategy Based on the Geometric Mean of Feature Importance and Robustness",
        "conference": "ACM The 2024 International Conference on Computer and Multimedia Technology (Conference Paper, Published)",
        "link": "https://dl.acm.org/doi/10.1145/3675249.3675335",
        "image": "static/paper1.jpg",
    },
    {
        "title": "Fault Diagnosis of Aero-engine Inter-shaft Bearings Using a Parallel SE-Depthwise Separable Convolutional Neural Network and Transformer Model",
        "conference": "IEEE 2024 7th International Conference on Mechatronics and Computer Technology Engineering (Conference Paper, Accepted for Publication)",
        "image": "static/paper2.jpg",
    },
    {
        "title": "LawLuo: A Multi-Agent Collaborative Framework for Chinese Legal Consultation",
        "conference": "arXiv (Conference Paper/CCF-A, Under Review)",
        "link": "https://arxiv.org/abs/2407.16252",
        "image": "static/paper3.jpg",
    },
    {
        "title": "Study on breast cancer image detection and classification based on residual connected convolutional neural network (CNN)",
        "conference": "2nd International Conference on Modern Medicine and Global Health (Conference Paper, Published)",
        "link": "https://www.ewadirect.com/proceedings/tns/article/view/10586",
        "image": "static/paper4.jpg",
    },
    {
        "title": "Multimodal Large Language Model Enhancement Network for Multimodal Sentiment Analysis",
        "conference": "Journal Paper (JCR-Q1, Under Review)",
        "image": "static/default_paper.jpg",
    },
    {
        "title": "Multi-Stage Simulation of Residents' Perception and Decision Making Behavior Regarding Disaster Risk Information: An Exploratory Study on Large Language Model Agents Driven Social-Cognitive Simulation Framework",
        "conference": "Journal Paper (JCR-Q1, Under Minor Revision)",
        "image": "static/default_paper.jpg",
    },
    {
        "title": "Swin Transformer with Large Margin Aware Focal Loss for Automatic Classification of Diabetic Retinopathy",
        "conference": "Journal Paper (Scopus-Q3, Under Major Revision)",
        "image": "static/default_paper.jpg",
    },
]

# 展示 Publications
for pub in publications:
    col1, col2 = st.columns([1, 3])

    with col1:
        # 显示论文封面图片
        st.image(pub["image"], width=150, use_column_width=True, caption="Paper Cover")

    with col2:
        # 论文信息
        st.markdown(
            f"""
            <div style="background-color: #2c2f33; padding: 15px; border-radius: 10px; box-shadow: 3px 3px 10px rgba(0,0,0,0.2); margin-bottom: 20px; color: #f1f1f1;">
                <h3 style="color: #4DB6AC;">{pub['title']}</h3>
                <p><b>Conference/Journal:</b> {pub['conference']}</p>
                {"<a href='" + pub['link'] + "' target='_blank' style='color: #64B5F6; text-decoration: none;'>Read Full Text 🔗</a>" if 'link' in pub else ""}
            </div>
            """,
            unsafe_allow_html=True,
        )

st.divider()
