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
    - **Universiti Tunku Abdul Rahman**  
      *Bachelor of Computer Science with Honours (Merit)*  
      📅 *2021-01 ~ 2024-09*  
      📍 *Kampar, Perak, Malaysia*
    """
)
st.markdown(
    """
    - **University of Sydney**  
      *Master of Computer Science (advanced entry)*  
      📅 *2025-08 ~ 2027-08*  
      📍 *Camperdown/Darlington, Sydney, Australia*
    """
)
st.divider()

# 工作经历
st.header("💼 Professional Experience")
st.markdown(
    """ 
     - **Artificial Intelligence Research Institute, China Academy of Information and Communications Technology (CAICT)**  
      *Artificial Intelligence Researcher*  
      📅 *2025-02 ~ Present*  
      📍 *Beijing, China*
            
    - **IFRC, Zhejiang University Binjiang Institute**  
      *Research Intern (Hybrid)*  
      📅 *2024-12 ~ Present*  
      📍 *Hangzhou, Zhejiang, China*
      
    - **AI Research Institute, Imperial Vision Group Co., Ltd.**  
      *Algorithm Engineer Intern*  
      📅 *2024-12 ~ 2025-02*  
      📍 *Fuzhou, Fujian, China*  

    - **Ruijie Networks**  
      *Technical Service Intern*  
      📅 *2023-10 ~ 2024-01*  
      📍 *Fuzhou, Fujian, China* 
    """
)
st.divider()

# 专业活动
st.header("🌟 Professional Activities")
st.markdown(
    """
    - **Reviewer, NeurIPS 2024 Workshop on Bayesian Decision-Making and Uncertainty**  
      📅 *2024-10*  

    - **Reviewer, International Joint Conference on Neural Networks (IJCNN) 2025**  
      📅 *2025-03*
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
