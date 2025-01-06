
import streamlit as st

# 页面配置
st.set_page_config(
    page_title="Daicx668 - Publications",
    page_icon="📚",
    layout="wide",
)

# 页面标题
st.title("📖 Publications")
st.markdown("欢迎来到我的学术成果展示页面！以下是我近年来在学术领域发表的一些成果。✨")

# 添加分割线
st.divider()

# 定义 publications 数据
publications = [
    {
        "title": "From the Perspective of Explainable Machine Learning: A Student Feature Selection Strategy Based on the Geometric Mean of Feature Importance and Robustness",
        "conference": "🎓 ACM The 2024 International Conference on Computer and Multimedia Technology (Published)",
        "link": "https://dl.acm.org/doi/10.1145/3675249.3675335",
    },
    {
        "title": "Fault Diagnosis of Aero-engine Inter-shaft Bearings Using a Parallel SE-Depthwise Separable Convolutional Neural Network and Transformer Model",
        "conference": "⚙️ IEEE 2024 7th International Conference on Mechatronics and Computer Technology Engineering (Accepted for Publication)",
    },
    {
        "title": "LawLuo: A Multi-Agent Collaborative Framework for Chinese Legal Consultation",
        "conference": "⚖️ arXiv (CCF-A, Under Review)",
        "link": "https://arxiv.org/abs/2407.16252",
    },
    {
        "title": "Study on breast cancer image detection and classification based on residual connected convolutional neural network (CNN)",
        "conference": "🧬 2nd International Conference on Modern Medicine and Global Health (Published)",
        "link": "https://www.ewadirect.com/proceedings/tns/article/view/10586",
    },
    {
        "title": "Multimodal Large Language Model Enhancement Network for Multimodal Sentiment Analysis",
        "conference": "💻 Journal Paper (JCR-Q1, Under Review)",
    },
    {
        "title": "Multi-Stage Simulation of Residents' Perception and Decision Making Behavior Regarding Disaster Risk Information: An Exploratory Study on Large Language Model Agents Driven Social-Cognitive Simulation Framework",
        "conference": "🏠 Journal Paper (JCR-Q1, Under Minor Revision)",
    },
    {
        "title": "Swin Transformer with Large Margin Aware Focal Loss for Automatic Classification of Diabetic Retinopathy",
        "conference": "🩺 Journal Paper (Scopus-Q3, Under Major Revision)",
    },
]

# 展示 publications
for idx, pub in enumerate(publications, start=1):
    st.markdown(
        f"""
        <div style="background-color: #f9f9f9; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
            <h4 style="color: #0078D4;">{idx}. {pub['title']}</h4>
            <p><b>Conference/Journal:</b> {pub['conference']}</p>
            {"<a href='" + pub['link'] + "' target='_blank' style='color: #FF6347; text-decoration: none;'>Read Full Text 🔗</a>" if 'link' in pub else ""}
        </div>
        """,
        unsafe_allow_html=True,
    )

