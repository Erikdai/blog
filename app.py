import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Daicx666",
    page_icon="🚀",
    layout="wide",
)

# Sidebar navigation
with st.sidebar:
    st.header("Menu")
    # Sidebar buttons
    if "page" not in st.session_state:
        st.session_state.page = "Home"  # Default to Home Page

    if st.button("🏠 Home"):
        st.session_state.page = "Home"
    if st.button("📜 Certificates"):
        st.session_state.page = "Certificates"

# 页面内容显示逻辑
if st.session_state.page == "Home":
    st.title("About me")
    st.divider()

    # Main content section
    st.markdown('<div class="main-content">', unsafe_allow_html=True)

    # Columns for layout
    col1, col2 = st.columns([1, 2], gap="medium")

    # Left column for profile image
    with col1:
        st.image("static/id.jpg", width=225, caption="DingDongJi")

    # Right column for detailed bio
    with col2:
        st.markdown(
            """
            <div class="about-text" style="margin-top: -10px;">
            😎 Hello! Welcome to my personal page :) I'm Dai, currently an Algorithm Engineer @ Imperial Vision and also a Research Intern @ the IFRC of Zhejiang University Binjiang Institute.
            My areas of interest include <span style="font-weight:bold;">Machine Learning (ML)</span>, <span style="font-weight:bold;">Large Language Models (LLMs)</span>, and <span style="font-weight:bold;">Natural Language Processing (NLP)</span>, <span style="font-weight:bold;">Computer Vision (CV)</span>. I have also conducted some research in <span style="font-weight:bold;">AI for Social Sciences (Cognitive Computing)</span> and <span style="font-weight:bold;">Signal Processing (Bearing Fault Detection)</span>.
            </div>
            """,
            unsafe_allow_html=True
        )

    # End of main content section
    st.markdown(""" """)
    st.divider()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "Certificates":
    try:
        import pages.certificates as certificates  # 动态加载 certificates.py
        certificates.display_certificates()  # 调用 certificates.py 中的函数
    except ModuleNotFoundError:
        st.error("The file 'certificates.py' was not found.")
