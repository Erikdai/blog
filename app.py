import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="Daicx666",
    page_icon="🚀",
    layout="wide",
)

# Add CSS for custom styling
st.markdown("""
    <style>
    /* Sidebar fixed and non-collapsible */
    [data-testid="collapsedControl"] {
        display: none;
    }

    /* Sidebar button styles */
    .sidebar-button {
        display: block;
        width: 100%;
        text-align: center;
        padding: 15px;
        margin: 5px 0;
        font-size: 18px;
        color: white;
        background-color: #007BFF;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }

    .sidebar-button:hover {
        background-color: #0056b3;
    }

    .sidebar-button.active {
        background-color: #004080;
    }

    /* Contact links */
    .contact-links {
        display: flex;
        justify-content: center; /* Center the links */
        align-items: center;
        gap: 30px; /* Space between links */
        margin-top: 20px;
        font-size: 16px;
    }
    .contact-links a {
        text-decoration: none;
        color: var(--text-color);
        display: inline-flex;
        align-items: center;
    }
    .contact-links a img {
        margin-right: 0px;
        width: 60px;
        height: 60px;
        border-radius: 50%;
    }
    .contact-links a:hover {
        text-decoration: underline;
        color: #007BFF; /* Blue color on hover */
    }

    /* Main content area */
    .main-content {
        max-width: 1000px;
        margin: 0 auto;
        padding: 20px;
    }

    /* About section layout */
    .about-col {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }

    .about-text {
        text-align: justify;
        font-size: 18px;
        line-height: 1.8;
        margin-top: 20px;
    }

    /* Responsive font size for smaller screens */
    @media (max-width: 768px) {
        .about-text {
            font-size: 16px;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.header("Menu")

    pages = {
        "🏠 Home": "Home",
        "📚 Experience": "Experience",
        "📖 Publications": "Publications",
        "🏆 Awards & Certificates": "Awards&Certificates",
    }

    if "page" not in st.session_state:
        st.session_state.page = "Home"

    for page_name, page_key in pages.items():
        # Sidebar buttons
        if st.button(page_name):
            st.session_state.page = page_key

# 页面内容显示逻辑
if st.session_state.page == "Home":
    # About Me Section (Home page)
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
            <div class="about-text" style="margin-top: -10px;"> <!-- 调整margin-top向上移动 -->
            😎 Hello! Welcome to my personal page :) I'm Dai, currently an Algorithm Engineer @ Imperial Vision and also a Research Intern @ the IFRC of Zhejiang University Binjiang Institute.
            My areas of interest include <span style="font-weight:bold;">Machine Learning (ML)</span>, <span style="font-weight:bold;">Large Language Models (LLMs)</span>, and <span style="font-weight:bold;">Natural Language Processing (NLP)</span>, <span style="font-weight:bold;">Computer Vision (CV)</span>. I have also conducted some research in <span style="font-weight:bold;">AI for Social Sciences (Cognitive Computing)</span> and <span style="font-weight:bold;">Signal Processing (Bearing Fault Detection)</span>.<br>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # End of main content section
    st.markdown(""" """)
    st.divider()
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer with social links
    st.markdown(
        """
        <div class="contact-links">
            <a href="https://www.kaggle.com/patpan" target="_blank">
                <img src="https://www.dataapplab.com/wp-content/uploads/2016/10/kaggle-logo-transparent-300-768x349.png" alt="Kaggle" style="height: 45px; margin-right: 7px;">Kaggle
            </a>
            <a href="https://www.linkedin.com/in/chengxiaodai" target="_blank">
                <img src="https://static.vecteezy.com/system/resources/previews/018/930/587/non_2x/linkedin-logo-linkedin-icon-transparent-free-png.png" alt="LinkedIn">LinkedIn
            </a>
            <a href="mailto:your_email@example.com">
                <img src="https://static.vecteezy.com/system/resources/thumbnails/018/972/241/small_2x/3d-message-icon-a-modern-email-concept-on-isolate-background-png.png" alt="Email" style="height: 45px; width: 45px; margin-right: 9px;">Email
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

elif st.session_state.page == "Experience":
    st.title("Experience Page")
    st.markdown("Welcome to the Experience Page!")

elif st.session_state.page == "Publications":
    st.title("Publications Page")
    st.markdown("Welcome to the Publications Page!")

elif st.session_state.page == "Awards&Certificates":
    st.title("Awards & Certificates")
    st.divider()

    # 加载 Markdown 文件内容
    try:
        with open("pages/awards_certificates.md", "r", encoding="utf-8") as file:
            md_content = file.read()
        st.markdown(md_content, unsafe_allow_html=True)  # 显示 Markdown 文件内容
    except FileNotFoundError:
        st.error("The file 'awards_certificates.md' was not found.")
