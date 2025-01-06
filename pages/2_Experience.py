import streamlit as st

# 页面配置
st.set_page_config(
    page_title="Daicx668 - Experience",
    page_icon="📚",
    layout="wide",
)

# 页面标题
st.title("📚 Experience")
st.divider()

# 教育背景
st.header("🎓 Education")
st.markdown(
    """
    - **Universiti Tunku Abdul Rahman (UTAR)**  
      *Bachelor of Computer Science with Honours (Merit)*  
      📅_2021-01 ~ 2024-09_   
      📍_Kampar, Perak, Malaysia_  
    """
)
st.divider()

# 工作经历
st.header("💼 Professional Experience")
st.markdown(
    """
    - **Ruijie Networks**  
      *Technical Service Intern*  
     📅 _2023-10 ~ 2024-01_    
     📍_Fuzhou, Fujian, China _  
      
    - **Imperial Vision Group Co., Ltd., AI Research Institute**  
      *Algorithm Engineer Intern*  
      📅_2024-12 ~ Present_    
      📍_Fuzhou, Fujian, China _  
      
    - **IFRC, Zhejiang University Binjiang Institute**  
      *Research Intern (Hybrid)*  
      📅_2024-12 ~ Present_    
      📍_Hangzhou, Zhejiang, China _  
    """
)
st.divider()

# 专业活动
st.header("🌟 Professional Activities")
st.markdown(
    """
    - **Reviewer, NeurIPS 2024 Workshop on Bayesian Decision-Making and Uncertainty** _- 2024_

    - **Reviewer, International Joint Conference on Neural Networks (IJCNN) 2025**  _-2025_
    """
)
st.divider()

# 页面美化
st.markdown(
    """
    <style>
    .main div.stMarkdown {
        font-family: Arial, sans-serif;
        font-size: 18px;
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
