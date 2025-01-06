import streamlit as st

# 页面配置
st.set_page_config(
    page_title="Daicx668 - Experience",
    page_icon="💼",
    layout="wide",
)

# 页面标题
st.title("💼 Experience")
st.markdown("以下是我的教育背景和工作经历，以及我参与的专业活动和学术贡献。✨")
st.divider()

# 教育背景
st.header("🎓 Education")
st.markdown(
    """
    - **Universiti Tunku Abdul Rahman (UTAR)**  
      *Bachelor of Computer Science with Honours (Merit)*  
      _2021-01 ~ 2024-09_  
      📍 Malaysia  
    """
)

# 工作经历
st.header("💼 Professional Experience")
st.markdown(
    """
    - **Ruijie Networks**  
      *Technical Service Intern*  
      _2023-10 ~ 2024-01_  
      📍 China  
      
    - **Imperial Vision Group Co., Ltd., AI Research Institute**  
      *Algorithm Intern*  
      _2024-12 ~ Present_  
      📍 China  
      
    - **IFRC, Zhejiang University Binjiang Institute**  
      *Research Intern (Hybrid)*  
      _2024-12 ~ Present_  
      📍 China  
    """
)

# 专业活动
st.header("🌟 Professional Activities")
st.markdown(
    """
    - **Reviewer, NeurIPS 2024 Workshop on Bayesian Decision-Making and Uncertainty**  
      _2024_

    - **Reviewer, International Joint Conference on Neural Networks (IJCNN) 2025**  
      _2025_
    """
)

# 页面美化
st.markdown(
    """
    <style>
    .main div.stMarkdown {
        font-family: Arial, sans-serif;
        font-size: 16px;
        line-height: 1.8;
    }
    .main h1 {
        color: #2E86C1;
        margin-bottom: 10px;
    }
    .main h2 {
        color: #117A65;
    }
    .main h3 {
        color: #E74C3C;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
